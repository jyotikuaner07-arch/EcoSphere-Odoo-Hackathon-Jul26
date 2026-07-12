from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.schemas.settings_schemas import EsgSettingsUpdate, NotificationSettingsUpdate
from app.services.settings_service import get_or_create_settings

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("/esg")
def get_esg_settings(session: Session = Depends(get_session)):
    s = get_or_create_settings(session)
    return {
        "weights": {
            "environmental": s.environmental_weight,
            "social": s.social_weight,
            "governance": s.governance_weight,
        },
        "auto_emission_calculation": s.auto_emission_calculation,
        "evidence_requirement": s.evidence_requirement,
        "badge_auto_award": s.badge_auto_award,
    }


@router.put("/esg")
def update_esg_settings(payload: EsgSettingsUpdate, session: Session = Depends(get_session)):
    s = get_or_create_settings(session)
    s.environmental_weight = payload.environmental_weight
    s.social_weight = payload.social_weight
    s.governance_weight = payload.governance_weight
    s.auto_emission_calculation = payload.auto_emission_calculation
    s.evidence_requirement = payload.evidence_requirement
    s.badge_auto_award = payload.badge_auto_award
    session.add(s)
    session.commit()
    session.refresh(s)
    return get_esg_settings(session)


@router.get("/notifications")
def get_notification_settings(session: Session = Depends(get_session)):
    s = get_or_create_settings(session)
    return {
        "compliance_issue_raised": s.notify_compliance_issue,
        "approval_decisions": s.notify_approval_decisions,
        "policy_reminders": s.notify_policy_reminders,
        "badge_unlocked": s.notify_badge_unlocked,
        "email_enabled": s.email_enabled,
    }


@router.put("/notifications")
def update_notification_settings(
    payload: NotificationSettingsUpdate,
    session: Session = Depends(get_session),
):
    s = get_or_create_settings(session)
    s.notify_compliance_issue = payload.notify_compliance_issue
    s.notify_approval_decisions = payload.notify_approval_decisions
    s.notify_policy_reminders = payload.notify_policy_reminders
    s.notify_badge_unlocked = payload.notify_badge_unlocked
    s.email_enabled = payload.email_enabled
    session.add(s)
    session.commit()
    return get_notification_settings(session)
