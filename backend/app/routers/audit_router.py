from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.models.audit import Audit
from app.services import audit_service

router = APIRouter(prefix="/audits", tags=["Audits"])


@router.get("", response_model=list[Audit])
def list_audits(session: Session = Depends(get_session)):
    return audit_service.list_audits(session)


@router.post("", response_model=Audit)
def create_audit(data: Audit, session: Session = Depends(get_session)):
    return audit_service.create_audit(session, data.model_dump(exclude={"id", "created_at"}))
