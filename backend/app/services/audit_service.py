from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.audit import Audit


def list_audits(session: Session) -> list[Audit]:
    return list(session.exec(select(Audit)).all())


def create_audit(session: Session, data: dict) -> Audit:
    audit = Audit(**data)
    session.add(audit)
    session.commit()
    session.refresh(audit)
    return audit


def get_audit(session: Session, audit_id: int) -> Audit:
    audit = session.get(Audit, audit_id)
    if not audit:
        raise NotFoundError("Audit", audit_id)
    return audit
