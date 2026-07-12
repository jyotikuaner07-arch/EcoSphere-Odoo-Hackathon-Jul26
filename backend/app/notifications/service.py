from sqlmodel import Session

from app.constants.enums import NotificationType
from app.models.notification import Notification
from app.models.settings import OrganizationSettings
from app.services.settings_service import get_or_create_settings


def create_notification(
    session: Session,
    *,
    employee_id: int,
    notification_type: NotificationType,
    title: str,
    message: str,
) -> Notification | None:
    settings = get_or_create_settings(session)

    type_enabled = {
        NotificationType.COMPLIANCE_ISSUE_RAISED: settings.notify_compliance_issue,
        NotificationType.APPROVAL_DECISION: settings.notify_approval_decisions,
        NotificationType.POLICY_ACKNOWLEDGEMENT_REMINDER: settings.notify_policy_reminders,
        NotificationType.BADGE_UNLOCKED: settings.notify_badge_unlocked,
    }

    if not type_enabled.get(notification_type, True):
        return None

    notification = Notification(
        employee_id=employee_id,
        type=notification_type,
        title=title,
        message=message,
    )
    session.add(notification)
    session.commit()
    session.refresh(notification)
    return notification
