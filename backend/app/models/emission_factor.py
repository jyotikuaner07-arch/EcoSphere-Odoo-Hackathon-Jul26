from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import GenericStatus, SourceType


class EmissionFactor(SQLModel, table=True):
    __tablename__ = "emission_factor"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=150)
    unit: str = Field(max_length=50)
    co2e_value: Decimal = Field(max_digits=10, decimal_places=4)
    source_type: SourceType
    status: GenericStatus = Field(default=GenericStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.utcnow)
