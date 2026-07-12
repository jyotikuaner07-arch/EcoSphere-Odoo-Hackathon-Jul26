from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import GenericStatus, RedemptionStatus


class Reward(SQLModel, table=True):
    __tablename__ = "rewards"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=150)
    description: Optional[str] = None
    points_required: int
    stock: Optional[int] = None
    status: GenericStatus = Field(default=GenericStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RewardRedemption(SQLModel, table=True):
    __tablename__ = "reward_redemptions"

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employees.id")
    reward_id: int = Field(foreign_key="rewards.id")
    points_spent: int
    redeemed_at: datetime = Field(default_factory=datetime.utcnow)
    status: RedemptionStatus = Field(default=RedemptionStatus.PENDING)
