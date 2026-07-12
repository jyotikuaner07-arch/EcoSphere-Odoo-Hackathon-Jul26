from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import CategoryType, GenericStatus


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True)
    type: CategoryType
    status: GenericStatus = Field(default=GenericStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.utcnow)
