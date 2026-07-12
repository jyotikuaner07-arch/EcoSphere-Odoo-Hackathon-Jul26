from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.constants.enums import ApprovalStatus, UserRole
from app.database import get_session
from app.dependencies import require_role
from app.models.participation import Participation
from app.models.user import User
from app.schemas.participation_schemas import ParticipationApprove
from app.services import participation_service

router = APIRouter(prefix="/participations", tags=["Participations"])


@router.post("/{participation_id}/approve", response_model=Participation)
def approve_participation(
    participation_id: int,
    payload: ParticipationApprove | None = None,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN, UserRole.DEPARTMENT_MANAGER)),
):
    data = payload or ParticipationApprove(approval_status=ApprovalStatus.APPROVED)
    return participation_service.approve_participation(session, participation_id, data)


@router.post("/{participation_id}/reject", response_model=Participation)
def reject_participation(
    participation_id: int,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN, UserRole.DEPARTMENT_MANAGER)),
):
    return participation_service.approve_participation(
        session,
        participation_id,
        ParticipationApprove(approval_status=ApprovalStatus.REJECTED),
    )
