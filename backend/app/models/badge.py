from datetime import datetime
from typing import Any, Optional

from sqlmodel import Column, Field, SQLModel
from sqlalchemy import JSON


class Badge(SQLModel, table=True):
    __tablename__ = "badges"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True)
    description: Optional[str] = None
    unlock_rule: Optional[dict[str, Any]] = Field(default=None, sa_column=Column(JSON))
    icon_url: Optional[str] = Field(default=None, max_length=500)
    status: str = Field(default="Active", max_length=20)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class EmployeeBadge(SQLModel, table=True):
    __tablename__ = "employee_badges"

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employees.id")
    badge_id: int = Field(foreign_key="badges.id")
    awarded_at: datetime = Field(default_factory=datetime.utcnow)
