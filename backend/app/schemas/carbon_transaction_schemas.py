from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.constants.enums import CalculationMode


class CarbonTransactionCreate(BaseModel):
    department_id: int
    emission_factor_id: int
    quantity: Decimal
    calculation_mode: CalculationMode = CalculationMode.AUTO
    source_reference: Optional[str] = None
    transaction_date: Optional[date] = None
