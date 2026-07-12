from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.models.badge import Badge
from app.schemas.badge_schemas import BadgeCreate
from app.services import badge_service

router = APIRouter(prefix="/badges", tags=["Badges"])


@router.get("", response_model=list[Badge])
def list_badges(session: Session = Depends(get_session)):
    return badge_service.list_badges(session)


@router.post("", response_model=Badge)
def create_badge(data: BadgeCreate, session: Session = Depends(get_session)):
    return badge_service.create_badge(session, data.model_dump())
