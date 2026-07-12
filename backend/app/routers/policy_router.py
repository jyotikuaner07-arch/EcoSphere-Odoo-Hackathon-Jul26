from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.dependencies import get_current_user
from app.models.policy import Policy, PolicyAcknowledgement
from app.models.user import User
from app.services import policy_service

router = APIRouter(prefix="/policies", tags=["Policies"])


@router.get("", response_model=list[Policy])
def list_policies(session: Session = Depends(get_session)):
    return policy_service.list_policies(session)


@router.post("", response_model=Policy)
def create_policy(data: Policy, session: Session = Depends(get_session)):
    return policy_service.create_policy(session, data.model_dump(exclude={"id", "created_at"}))


@router.post("/{policy_id}/acknowledge", response_model=PolicyAcknowledgement)
def acknowledge_policy(
    policy_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return policy_service.acknowledge_policy(session, policy_id, current_user)
