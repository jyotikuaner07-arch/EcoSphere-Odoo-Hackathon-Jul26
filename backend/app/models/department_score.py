from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel


class DepartmentScore(SQLModel, table=True):
    __tablename__ = "department_score"

    id: Optional[int] = Field(default=None, primary_key=True)
    department_id: int = Field(foreign_key="departments.id")
    environmental_score: Decimal = Field(default=Decimal("0.00"), max_digits=5, decimal_places=2)
    social_score: Decimal = Field(default=Decimal("0.00"), max_digits=5, decimal_places=2)
    governance_score: Decimal = Field(default=Decimal("0.00"), max_digits=5, decimal_places=2)
    total_score: Decimal = Field(default=Decimal("0.00"), max_digits=5, decimal_places=2)
    period: Optional[str] = Field(default=None, max_length=20)
    calculated_at: datetime = Field(default_factory=datetime.utcnow)
