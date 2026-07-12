from sqlmodel import Session, select

from app.models.notification import Notification
from app.models.user import User


def list_notifications(session: Session, user: User) -> list[Notification]:
    return list(
        session.exec(
            select(Notification)
            .where(Notification.employee_id == user.id)
            .order_by(Notification.created_at.desc())
        ).all()
    )


def mark_notification_read(session: Session, notification_id: int, user: User) -> Notification:
    notification = session.get(Notification, notification_id)
    if not notification or notification.employee_id != user.id:
        from app.core.exceptions import NotFoundError
        raise NotFoundError("Notification", notification_id)

    notification.is_read = True
    session.add(notification)
    session.commit()
    session.refresh(notification)
    return notification
