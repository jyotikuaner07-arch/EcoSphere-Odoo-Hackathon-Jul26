from datetime import date as date_type, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import CsrActivityStatus


class CsrActivity(SQLModel, table=True):
    __tablename__ = "csr_activity"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200)
    category_id: int = Field(foreign_key="categories.id")
    department_id: int = Field(foreign_key="departments.id")
    description: Optional[str] = None
    date: Optional[date_type] = None
    points: int = Field(default=50)
    status: CsrActivityStatus = Field(default=CsrActivityStatus.DRAFT)
    created_at: datetime = Field(default_factory=datetime.utcnow)
