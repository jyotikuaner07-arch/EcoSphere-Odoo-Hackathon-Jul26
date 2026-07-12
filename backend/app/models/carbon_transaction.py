from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import CalculationMode


class CarbonTransaction(SQLModel, table=True):
    __tablename__ = "carbon_transaction"

    id: Optional[int] = Field(default=None, primary_key=True)
    department_id: int = Field(foreign_key="departments.id")
    emission_factor_id: int = Field(foreign_key="emission_factor.id")
    quantity: Decimal = Field(max_digits=12, decimal_places=4)
    co2e_kg: Decimal = Field(max_digits=12, decimal_places=4)
    calculation_mode: CalculationMode = Field(default=CalculationMode.AUTO)
    source_reference: Optional[str] = Field(default=None, max_length=200)
    transaction_date: Optional[date] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
