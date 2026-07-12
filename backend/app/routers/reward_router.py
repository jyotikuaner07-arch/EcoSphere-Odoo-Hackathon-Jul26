from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.dependencies import get_current_user
from app.models.reward import Reward, RewardRedemption
from app.models.user import User
from app.services import reward_service

router = APIRouter(prefix="/rewards", tags=["Rewards"])


@router.get("", response_model=list[Reward])
def list_rewards(session: Session = Depends(get_session)):
    return reward_service.list_rewards(session)


@router.post("", response_model=Reward)
def create_reward(data: Reward, session: Session = Depends(get_session)):
    return reward_service.create_reward(session, data.model_dump(exclude={"id", "created_at"}))


@router.post("/{reward_id}/redeem", response_model=RewardRedemption)
def redeem_reward(
    reward_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return reward_service.redeem_reward(session, reward_id, current_user)
