from typing import Optional

from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.environmental_goal import EnvironmentalGoal


def list_goals(session: Session, department_id: Optional[int] = None) -> list[EnvironmentalGoal]:
    query = select(EnvironmentalGoal)
    if department_id:
        query = query.where(EnvironmentalGoal.department_id == department_id)
    return list(session.exec(query).all())


def create_goal(session: Session, data: dict) -> EnvironmentalGoal:
    goal = EnvironmentalGoal(**data)
    session.add(goal)
    session.commit()
    session.refresh(goal)
    return goal


def get_goal(session: Session, goal_id: int) -> EnvironmentalGoal:
    goal = session.get(EnvironmentalGoal, goal_id)
    if not goal:
        raise NotFoundError("EnvironmentalGoal", goal_id)
    return goal
