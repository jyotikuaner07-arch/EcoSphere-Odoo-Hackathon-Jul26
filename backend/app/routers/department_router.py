from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.constants.enums import UserRole
from app.database import get_session
from app.dependencies import get_current_user, require_role
from app.models.department import Department
from app.models.user import User
from app.services import department_service, scoring_service

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get("", response_model=list[Department])
def list_departments(session: Session = Depends(get_session)):
    return department_service.list_departments(session)


@router.get("/{department_id}", response_model=Department)
def get_department(department_id: int, session: Session = Depends(get_session)):
    return department_service.get_department(session, department_id)


@router.post("", response_model=Department)
def create_department(
    data: Department,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN)),
):
    return department_service.create_department(session, data.model_dump(exclude={"id", "created_at"}))


@router.put("/{department_id}", response_model=Department)
def update_department(
    department_id: int,
    data: Department,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN)),
):
    return department_service.update_department(
        session,
        department_id,
        data.model_dump(exclude={"id", "created_at"}, exclude_unset=True),
    )


@router.get("/{department_id}/score")
def department_score(department_id: int, session: Session = Depends(get_session)):
    return scoring_service.calculate_department_score(session, department_id)
