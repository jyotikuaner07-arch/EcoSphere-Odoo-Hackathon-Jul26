from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.department import Department


def list_departments(session: Session) -> list[Department]:
    return list(session.exec(select(Department)).all())


def get_department(session: Session, department_id: int) -> Department:
    dept = session.get(Department, department_id)
    if not dept:
        raise NotFoundError("Department", department_id)
    return dept


def create_department(session: Session, data: dict) -> Department:
    dept = Department(**data)
    session.add(dept)
    session.commit()
    session.refresh(dept)
    return dept


def update_department(session: Session, department_id: int, data: dict) -> Department:
    dept = get_department(session, department_id)
    for key, value in data.items():
        if value is not None and hasattr(dept, key):
            setattr(dept, key, value)
    session.add(dept)
    session.commit()
    session.refresh(dept)
    return dept


def delete_department(session: Session, department_id: int) -> None:
    dept = get_department(session, department_id)
    session.delete(dept)
    session.commit()
