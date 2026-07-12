from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.database import get_session
from app.services import dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(session: Session = Depends(get_session)):
    return dashboard_service.get_dashboard_summary(session)


@router.get("/leaderboard")
def leaderboard(
    department_id: Optional[int] = Query(default=None),
    period: Optional[str] = Query(default=None),
    session: Session = Depends(get_session),
):
    return dashboard_service.get_leaderboard(session, department_id, period)


router_leaderboard = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])


@router_leaderboard.get("")
def leaderboard_alias(
    department_id: Optional[int] = Query(default=None),
    period: Optional[str] = Query(default=None),
    session: Session = Depends(get_session),
):
    return dashboard_service.get_leaderboard(session, department_id, period)
