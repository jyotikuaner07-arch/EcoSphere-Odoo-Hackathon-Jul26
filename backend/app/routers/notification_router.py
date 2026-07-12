from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.database import get_session
from app.dependencies import get_current_user
from app.models.notification import Notification
from app.models.user import User
from app.reports.service import build_report_summary
from app.services import notification_service

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("", response_model=list[Notification])
def list_notifications(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return notification_service.list_notifications(session, current_user)


@router.patch("/{notification_id}/read", response_model=Notification)
def mark_read(
    notification_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return notification_service.mark_notification_read(session, notification_id, current_user)
