from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import GenericStatus


class Department(SQLModel, table=True):
    __tablename__ = "departments"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    code: Optional[str] = Field(default=None, max_length=20, unique=True)
    head_employee_id: Optional[int] = Field(default=None, foreign_key="employees.id")
    parent_department_id: Optional[int] = Field(default=None, foreign_key="departments.id")
    employee_count: int = Field(default=0)
    status: GenericStatus = Field(default=GenericStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.utcnow)
