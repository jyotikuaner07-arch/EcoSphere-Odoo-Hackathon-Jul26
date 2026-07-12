from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import GoalStatus


class EnvironmentalGoal(SQLModel, table=True):
    __tablename__ = "environmental_goal"

    id: Optional[int] = Field(default=None, primary_key=True)
    department_id: int = Field(foreign_key="departments.id")
    metric_type: str = Field(max_length=100)
    target_value: Decimal = Field(max_digits=12, decimal_places=2)
    current_value: Decimal = Field(default=Decimal("0.00"), max_digits=12, decimal_places=2)
    deadline: Optional[date] = None
    status: GoalStatus = Field(default=GoalStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.utcnow)
