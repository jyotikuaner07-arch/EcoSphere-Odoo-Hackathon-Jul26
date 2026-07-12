from datetime import date as date_type, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import AuditStatus


class Audit(SQLModel, table=True):
    __tablename__ = "audit"

    id: Optional[int] = Field(default=None, primary_key=True)
    department_id: int = Field(foreign_key="departments.id")
    title: str = Field(max_length=200)
    description: Optional[str] = None
    auditor: Optional[str] = Field(default=None, max_length=150)
    status: AuditStatus = Field(default=AuditStatus.SCHEDULED)
    date: Optional[date_type] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
