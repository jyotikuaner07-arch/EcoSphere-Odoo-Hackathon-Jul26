from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.database import get_session
from app.models.environmental_goal import EnvironmentalGoal
from app.services import goal_service

router = APIRouter(prefix="/goals", tags=["Environmental Goals"])


@router.get("", response_model=list[EnvironmentalGoal])
def list_goals(
    department_id: Optional[int] = Query(default=None),
    session: Session = Depends(get_session),
):
    return goal_service.list_goals(session, department_id)


@router.post("", response_model=EnvironmentalGoal)
def create_goal(data: EnvironmentalGoal, session: Session = Depends(get_session)):
    return goal_service.create_goal(session, data.model_dump(exclude={"id", "created_at"}))
