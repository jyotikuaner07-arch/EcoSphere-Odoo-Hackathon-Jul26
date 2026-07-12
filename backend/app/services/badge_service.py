from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.badge import Badge, EmployeeBadge


def list_badges(session: Session) -> list[Badge]:
    return list(session.exec(select(Badge)).all())


def create_badge(session: Session, data: dict) -> Badge:
    badge = Badge(**data)
    session.add(badge)
    session.commit()
    session.refresh(badge)
    return badge


def get_employee_badges(session: Session, employee_id: int) -> list[Badge]:
    rows = session.exec(
        select(Badge)
        .join(EmployeeBadge, EmployeeBadge.badge_id == Badge.id)
        .where(EmployeeBadge.employee_id == employee_id)
    ).all()
    return list(rows)


def get_badge(session: Session, badge_id: int) -> Badge:
    badge = session.get(Badge, badge_id)
    if not badge:
        raise NotFoundError("Badge", badge_id)
    return badge
