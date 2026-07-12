from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.dependencies import get_current_user
from app.models.reward import Reward
from app.models.user import User
from app.services import badge_service, auth_service, reward_service

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/{employee_id}/xp")
def get_employee_xp(employee_id: int, session: Session = Depends(get_session)):
    user = auth_service.get_user(session, employee_id)
    return {"employee_id": user.id, "xp_points": user.xp_points}


@router.get("/{employee_id}/badges", response_model=list)
def get_employee_badges(employee_id: int, session: Session = Depends(get_session)):
    return badge_service.get_employee_badges(session, employee_id)
