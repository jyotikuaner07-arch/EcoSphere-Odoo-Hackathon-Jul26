"""Import all models so SQLModel.metadata.create_all registers every table."""

from app.models.user import User
from app.models.department import Department
from app.models.category import Category
from app.models.emission_factor import EmissionFactor
from app.models.carbon_transaction import CarbonTransaction
from app.models.environmental_goal import EnvironmentalGoal
from app.models.csr_activity import CsrActivity
from app.models.participation import Participation
from app.models.challenge import Challenge
from app.models.challenge_participation import ChallengeParticipation
from app.models.badge import Badge, EmployeeBadge
from app.models.reward import Reward, RewardRedemption
from app.models.policy import Policy, PolicyAcknowledgement
from app.models.audit import Audit
from app.models.compliance_issue import ComplianceIssue
from app.models.department_score import DepartmentScore
from app.models.notification import Notification
from app.models.settings import OrganizationSettings

__all__ = [
    "User",
    "Department",
    "Category",
    "EmissionFactor",
    "CarbonTransaction",
    "EnvironmentalGoal",
    "CsrActivity",
    "Participation",
    "Challenge",
    "ChallengeParticipation",
    "Badge",
    "EmployeeBadge",
    "Reward",
    "RewardRedemption",
    "Policy",
    "PolicyAcknowledgement",
    "Audit",
    "ComplianceIssue",
    "DepartmentScore",
    "Notification",
    "OrganizationSettings",
]
