from decimal import Decimal
from typing import Optional

from sqlmodel import Session, select

from app.constants.enums import CalculationMode
from app.core.exceptions import NoEmissionFactorConfiguredError, NotFoundError
from app.models.carbon_transaction import CarbonTransaction
from app.models.emission_factor import EmissionFactor
from app.schemas.carbon_transaction_schemas import CarbonTransactionCreate
from app.services.settings_service import get_or_create_settings


def list_carbon_transactions(
    session: Session,
    department_id: Optional[int] = None,
) -> list[CarbonTransaction]:
    query = select(CarbonTransaction)
    if department_id:
        query = query.where(CarbonTransaction.department_id == department_id)
    return list(session.exec(query).all())


def create_transaction(session: Session, payload: CarbonTransactionCreate) -> CarbonTransaction:
    factor = session.get(EmissionFactor, payload.emission_factor_id)
    if not factor:
        raise NoEmissionFactorConfiguredError()

    settings = get_or_create_settings(session)
    mode = payload.calculation_mode
    if settings.auto_emission_calculation and mode == CalculationMode.AUTO:
        co2e = payload.quantity * factor.co2e_value
    else:
        co2e = payload.quantity * factor.co2e_value

    tx = CarbonTransaction(
        department_id=payload.department_id,
        emission_factor_id=payload.emission_factor_id,
        quantity=payload.quantity,
        co2e_kg=Decimal(co2e),
        calculation_mode=mode,
        source_reference=payload.source_reference,
        transaction_date=payload.transaction_date,
    )
    session.add(tx)
    session.commit()
    session.refresh(tx)
    return tx


def get_transaction(session: Session, tx_id: int) -> CarbonTransaction:
    tx = session.get(CarbonTransaction, tx_id)
    if not tx:
        raise NotFoundError("CarbonTransaction", tx_id)
    return tx
