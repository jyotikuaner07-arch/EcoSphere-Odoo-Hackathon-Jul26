from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.database import get_session
from app.models.carbon_transaction import CarbonTransaction
from app.schemas.carbon_transaction_schemas import CarbonTransactionCreate
from app.services import carbon_transaction_service

router = APIRouter(prefix="/carbon-transactions", tags=["Carbon Transactions"])


@router.get("", response_model=list[CarbonTransaction])
def list_transactions(
    department_id: Optional[int] = Query(default=None),
    session: Session = Depends(get_session),
):
    return carbon_transaction_service.list_carbon_transactions(session, department_id)


@router.post("", response_model=CarbonTransaction)
def create_transaction(payload: CarbonTransactionCreate, session: Session = Depends(get_session)):
    return carbon_transaction_service.create_transaction(session, payload)
