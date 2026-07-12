from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import AcknowledgementStatus, PolicyStatus


class Policy(SQLModel, table=True):
    __tablename__ = "esg_policy"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200)
    description: Optional[str] = None
    document_url: Optional[str] = Field(default=None, max_length=500)
    version: Optional[str] = Field(default=None, max_length=20)
    status: PolicyStatus = Field(default=PolicyStatus.DRAFT)
    effective_date: Optional[date] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PolicyAcknowledgement(SQLModel, table=True):
    __tablename__ = "policy_acknowledgement"

    id: Optional[int] = Field(default=None, primary_key=True)
    policy_id: int = Field(foreign_key="esg_policy.id")
    employee_id: int = Field(foreign_key="employees.id")
    acknowledged_at: Optional[datetime] = None
    status: AcknowledgementStatus = Field(default=AcknowledgementStatus.PENDING)
