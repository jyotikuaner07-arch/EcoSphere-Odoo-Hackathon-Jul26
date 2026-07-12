from sqlmodel import Session, select

from app.core.exceptions import InsufficientPointsError, NotFoundError, OutOfStockError
from app.models.reward import Reward, RewardRedemption
from app.models.user import User


def list_rewards(session: Session) -> list[Reward]:
    return list(session.exec(select(Reward)).all())


def create_reward(session: Session, data: dict) -> Reward:
    reward = Reward(**data)
    session.add(reward)
    session.commit()
    session.refresh(reward)
    return reward


def redeem_reward(session: Session, reward_id: int, user: User) -> RewardRedemption:
    reward = session.get(Reward, reward_id)
    if not reward:
        raise NotFoundError("Reward", reward_id)

    if reward.stock is not None and reward.stock <= 0:
        raise OutOfStockError()

    if user.xp_points < reward.points_required:
        raise InsufficientPointsError()

    user.xp_points -= reward.points_required
    if reward.stock is not None:
        reward.stock -= 1

    redemption = RewardRedemption(
        employee_id=user.id,
        reward_id=reward.id,
        points_spent=reward.points_required,
    )
    session.add(user)
    session.add(reward)
    session.add(redemption)
    session.commit()
    session.refresh(redemption)
    return redemption
