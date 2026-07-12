from datetime import date

from sqlmodel import Session, select

from app.constants.enums import ApprovalStatus, NotificationType
from app.core.exceptions import EvidenceRequiredError, NotFoundError
from app.models.participation import Participation
from app.models.user import User
from app.notifications.service import create_notification
from app.schemas.participation_schemas import ParticipationApprove, ParticipationJoin
from app.services.csr_activity_service import get_csr_activity
from app.services.settings_service import get_or_create_settings
from app.utils.badge_checker import check_and_award_badges


def join_activity(session: Session, activity_id: int, user: User, payload: ParticipationJoin) -> Participation:
    get_csr_activity(session, activity_id)
    existing = session.exec(
        select(Participation).where(
            Participation.activity_id == activity_id,
            Participation.employee_id == user.id,
        )
    ).first()
    if existing:
        return existing

    participation = Participation(
        employee_id=user.id,
        activity_id=activity_id,
        proof_url=payload.proof_url,
    )
    session.add(participation)
    session.commit()
    session.refresh(participation)
    return participation


def approve_participation(
    session: Session,
    participation_id: int,
    payload: ParticipationApprove,
) -> Participation:
    participation = session.get(Participation, participation_id)
    if not participation:
        raise NotFoundError("Participation", participation_id)

    settings = get_or_create_settings(session)
    if (
        settings.evidence_requirement
        and payload.approval_status == ApprovalStatus.APPROVED
        and not participation.proof_url
    ):
        raise EvidenceRequiredError()

    activity = get_csr_activity(session, participation.activity_id)
    points = payload.points_earned if payload.points_earned is not None else activity.points

    participation.approval_status = payload.approval_status
    if payload.approval_status == ApprovalStatus.APPROVED:
        participation.points_earned = points
        participation.completion_date = date.today()

        user = session.get(User, participation.employee_id)
        if user:
            user.xp_points += points
            session.add(user)

    session.add(participation)
    session.commit()
    session.refresh(participation)

    if payload.approval_status in (ApprovalStatus.APPROVED, ApprovalStatus.REJECTED):
        create_notification(
            session,
            employee_id=participation.employee_id,
            notification_type=NotificationType.APPROVAL_DECISION,
            title="CSR Participation Update",
            message=f"Your CSR participation was {payload.approval_status.value}.",
        )

    if payload.approval_status == ApprovalStatus.APPROVED:
        settings = get_or_create_settings(session)
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
