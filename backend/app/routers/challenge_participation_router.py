from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.constants.enums import ApprovalStatus, UserRole
from app.database import get_session
from app.dependencies import require_role
from app.models.challenge_participation import ChallengeParticipation
from app.models.user import User
from app.schemas.challenge_schemas import ChallengeParticipationApprove, ChallengeParticipationProgress
from app.services import challenge_participation_service

router = APIRouter(prefix="/challenge-participations", tags=["Challenge Participations"])


@router.patch("/{participation_id}/progress", response_model=ChallengeParticipation)
def update_progress(
    participation_id: int,
    payload: ChallengeParticipationProgress,
    session: Session = Depends(get_session),
):
    return challenge_participation_service.update_progress(session, participation_id, payload)


@router.post("/{participation_id}/approve", response_model=ChallengeParticipation)
def approve_participation(
    participation_id: int,
    payload: ChallengeParticipationApprove | None = None,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN, UserRole.SUSTAINABILITY_OFFICER)),
):
    data = payload or ChallengeParticipationApprove(approval_status=ApprovalStatus.APPROVED)
    return challenge_participation_service.approve_challenge_participation(
        session, participation_id, data
    )
