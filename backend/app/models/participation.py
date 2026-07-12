from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import ApprovalStatus


class Participation(SQLModel, table=True):
    __tablename__ = "employee_participation"

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employees.id")
    activity_id: int = Field(foreign_key="csr_activity.id")
    proof_url: Optional[str] = Field(default=None, max_length=500)
    approval_status: ApprovalStatus = Field(default=ApprovalStatus.PENDING)
    points_earned: int = Field(default=0)
    completion_date: Optional[date] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
