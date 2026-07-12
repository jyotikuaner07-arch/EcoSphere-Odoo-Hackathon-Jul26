from typing import Optional

from sqlmodel import Field, SQLModel


class OrganizationSettings(SQLModel, table=True):
    """Singleton row (id=1) holding org-wide ESG and notification toggles."""

    __tablename__ = "organization_settings"

    id: Optional[int] = Field(default=1, primary_key=True)
    environmental_weight: int = Field(default=40)
    social_weight: int = Field(default=30)
    governance_weight: int = Field(default=30)
    auto_emission_calculation: bool = Field(default=True)
    evidence_requirement: bool = Field(default=True)
    badge_auto_award: bool = Field(default=True)
    notify_compliance_issue: bool = Field(default=True)
    notify_approval_decisions: bool = Field(default=True)
    notify_policy_reminders: bool = Field(default=True)
    notify_badge_unlocked: bool = Field(default=True)
    email_enabled: bool = Field(default=False)
