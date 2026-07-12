from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import NotificationType


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employees.id")
    type: NotificationType
    title: str = Field(max_length=200)
    message: str
    is_read: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
