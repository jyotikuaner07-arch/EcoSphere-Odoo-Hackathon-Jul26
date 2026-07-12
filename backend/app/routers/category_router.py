from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.constants.enums import CategoryType, UserRole
from app.database import get_session
from app.dependencies import require_role
from app.models.category import Category
from app.models.user import User
from app.services import category_service

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("", response_model=list[Category])
def list_categories(
    type: Optional[CategoryType] = Query(default=None),
    session: Session = Depends(get_session),
):
    return category_service.list_categories(session, type)


@router.post("", response_model=Category)
def create_category(
    data: Category,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN)),
):
    return category_service.create_category(session, data.model_dump(exclude={"id", "created_at"}))
