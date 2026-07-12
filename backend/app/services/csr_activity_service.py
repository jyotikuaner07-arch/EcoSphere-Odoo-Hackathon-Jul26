from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.csr_activity import CsrActivity


def list_csr_activities(session: Session) -> list[CsrActivity]:
    return list(session.exec(select(CsrActivity)).all())


def create_csr_activity(session: Session, data: dict) -> CsrActivity:
    activity = CsrActivity(**data)
    session.add(activity)
    session.commit()
    session.refresh(activity)
    return activity


def get_csr_activity(session: Session, activity_id: int) -> CsrActivity:
    activity = session.get(CsrActivity, activity_id)
    if not activity:
        raise NotFoundError("CsrActivity", activity_id)
    return activity
