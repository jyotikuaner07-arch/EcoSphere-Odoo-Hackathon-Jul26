from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import ComplianceIssueStatus, Severity


class ComplianceIssue(SQLModel, table=True):
    __tablename__ = "compliance_issue"

    id: Optional[int] = Field(default=None, primary_key=True)
    audit_id: Optional[int] = Field(default=None, foreign_key="audit.id")
    department_id: int = Field(foreign_key="departments.id")
    severity: Severity = Field(default=Severity.LOW)
    description: Optional[str] = None
    owner_employee_id: Optional[int] = Field(default=None, foreign_key="employees.id")
    due_date: Optional[date] = None
    status: ComplianceIssueStatus = Field(default=ComplianceIssueStatus.OPEN)
    raised_at: datetime = Field(default_factory=datetime.utcnow)
