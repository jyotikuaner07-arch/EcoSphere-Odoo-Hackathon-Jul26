from sqlmodel import Session, select

from app.constants.enums import ApprovalStatus, NotificationType
from app.core.exceptions import EvidenceRequiredError, NotFoundError
from app.models.challenge_participation import ChallengeParticipation
from app.models.user import User
from app.notifications.service import create_notification
from app.schemas.challenge_schemas import (
    ChallengeParticipationApprove,
    ChallengeParticipationJoin,
    ChallengeParticipationProgress,
)
from app.services.challenge_service import get_challenge
from app.services.settings_service import get_or_create_settings
from app.utils.badge_checker import check_and_award_badges


def join_challenge(
    session: Session,
    challenge_id: int,
    user: User,
    payload: ChallengeParticipationJoin,
) -> ChallengeParticipation:
    get_challenge(session, challenge_id)
    existing = session.exec(
        select(ChallengeParticipation).where(
            ChallengeParticipation.challenge_id == challenge_id,
            ChallengeParticipation.employee_id == user.id,
        )
    ).first()
    if existing:
        return existing

    participation = ChallengeParticipation(
        challenge_id=challenge_id,
        employee_id=user.id,
        proof_url=payload.proof_url,
    )
    session.add(participation)
    session.commit()
    session.refresh(participation)
    return participation


def update_progress(
    session: Session,
    participation_id: int,
    payload: ChallengeParticipationProgress,
) -> ChallengeParticipation:
    participation = session.get(ChallengeParticipation, participation_id)
    if not participation:
        raise NotFoundError("ChallengeParticipation", participation_id)

    participation.progress = payload.progress
    if payload.proof_url:
        participation.proof_url = payload.proof_url

    session.add(participation)
    session.commit()
    session.refresh(participation)
    return participation


def approve_challenge_participation(
    session: Session,
    participation_id: int,
    payload: ChallengeParticipationApprove,
) -> ChallengeParticipation:
    participation = session.get(ChallengeParticipation, participation_id)
    if not participation:
        raise NotFoundError("ChallengeParticipation", participation_id)

    challenge = get_challenge(session, participation.challenge_id)
    settings = get_or_create_settings(session)

    if (
        settings.evidence_requirement
        and payload.approval_status == ApprovalStatus.APPROVED
        and challenge.evidence_required
        and not participation.proof_url
    ):
        raise EvidenceRequiredError()

    participation.approval_status = payload.approval_status
    if payload.approval_status == ApprovalStatus.APPROVED:
        participation.xp_awarded = challenge.xp
        participation.progress = 100

        user = session.get(User, participation.employee_id)
        if user:
            user.xp_points += challenge.xp
            session.add(user)

    session.add(participation)
    session.commit()
    session.refresh(participation)

    create_notification(
        session,
        employee_id=participation.employee_id,
        notification_type=NotificationType.APPROVAL_DECISION,
        title="Challenge Participation Update",
        message=f"Your challenge participation was {payload.approval_status.value}.",
    )

    if payload.approval_status == ApprovalStatus.APPROVED:
        awarded = check_and_award_badges(session, participation.employee_id, settings.badge_auto_award)
        for badge in awarded:
            create_notification(
                session,
                employee_id=participation.employee_id,
                notification_type=NotificationType.BADGE_UNLOCKED,
                title="Badge Unlocked!",
                message=f"You earned the {badge.name} badge.",
            )

    return participation
