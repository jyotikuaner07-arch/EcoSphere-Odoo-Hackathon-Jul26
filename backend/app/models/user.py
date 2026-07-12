from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import GenericStatus, UserRole


class User(SQLModel, table=True):
    __tablename__ = "employees"

    id: Optional[int] = Field(default=None, primary_key=True)
    department_id: int = Field(foreign_key="departments.id")
    name: str = Field(max_length=100)
    email: str = Field(max_length=150, unique=True, index=True)
    password_hash: str = Field(max_length=255)
    role: UserRole = Field(default=UserRole.EMPLOYEE)
    xp_points: int = Field(default=0)
    join_date: Optional[date] = None
    status: GenericStatus = Field(default=GenericStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.utcnow)
