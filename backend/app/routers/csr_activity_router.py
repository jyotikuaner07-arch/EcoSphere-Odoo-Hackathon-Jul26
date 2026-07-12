from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.dependencies import get_current_user
from app.models.csr_activity import CsrActivity
from app.models.participation import Participation
from app.models.user import User
from app.schemas.participation_schemas import ParticipationJoin
from app.services import csr_activity_service, participation_service

router = APIRouter(prefix="/csr-activities", tags=["CSR Activities"])


@router.get("", response_model=list[CsrActivity])
def list_activities(session: Session = Depends(get_session)):
    return csr_activity_service.list_csr_activities(session)


@router.post("", response_model=CsrActivity)
def create_activity(data: CsrActivity, session: Session = Depends(get_session)):
    return csr_activity_service.create_csr_activity(
        session, data.model_dump(exclude={"id", "created_at"})
    )


@router.post("/{activity_id}/join", response_model=Participation)
def join_activity(
    activity_id: int,
    payload: ParticipationJoin,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return participation_service.join_activity(session, activity_id, current_user, payload)
