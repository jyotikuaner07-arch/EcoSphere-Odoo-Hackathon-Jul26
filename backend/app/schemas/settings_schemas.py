from pydantic import BaseModel, Field


class EsgSettingsUpdate(BaseModel):
    environmental_weight: int = Field(ge=0, le=100)
    social_weight: int = Field(ge=0, le=100)
    governance_weight: int = Field(ge=0, le=100)
    auto_emission_calculation: bool = True
    evidence_requirement: bool = True
    badge_auto_award: bool = True


class NotificationSettingsUpdate(BaseModel):
    notify_compliance_issue: bool = True
    notify_approval_decisions: bool = True
    notify_policy_reminders: bool = True
    notify_badge_unlocked: bool = True
    email_enabled: bool = False
