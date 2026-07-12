"""
constants/enums.py

Single source of truth for every role and status value used across EcoSphere.

Why this file exists:
- Every model, schema, and service imports from here instead of hardcoding
  raw strings like "Approved" or "Admin" in multiple places.
- These exact string values are also what the frontend team will send/receive
  in API requests and responses - if this file changes, the frontend must
  be updated too. Treat this as a shared contract, not an internal detail.

We inherit from (str, Enum) rather than plain Enum so that:
1. FastAPI/Pydantic can serialize these directly to plain JSON strings
   (e.g. "Draft" instead of "ChallengeStatus.DRAFT").
2. SQLModel can store them as native string columns in MySQL.
3. Comparisons like `status == "Approved"` still work naturally.
"""

from enum import Enum


class UserRole(str, Enum):
    """Every actor type in the system, as defined in the problem statement."""
    ADMIN = "Admin"
    SUSTAINABILITY_OFFICER = "Sustainability Officer"
    COMPLIANCE_OFFICER = "Compliance Officer"
    DEPARTMENT_MANAGER = "Department Manager"
    EMPLOYEE = "Employee"
    MANAGEMENT = "Management"


class CategoryType(str, Enum):
    """Category.type field - shared category values used by CSR Activities and Challenges."""
    CSR_ACTIVITY = "CSR_ACTIVITY"
    CHALLENGE = "CHALLENGE"


class ApprovalStatus(str, Enum):
    """
    Used by both Participation (CSR) and ChallengeParticipation.
    Kept as one shared enum since the approval workflow is identical in both cases.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ChallengeStatus(str, Enum):
    """
    Full lifecycle of a Challenge, as defined in the problem statement:
    Draft -> Active -> Under Review -> Completed, or Archived at any point.
    """
    DRAFT = "Draft"
    ACTIVE = "Active"
    UNDER_REVIEW = "Under Review"
    COMPLETED = "Completed"
    ARCHIVED = "Archived"


class CalculationMode(str, Enum):
    """
    How a Carbon Transaction's co2e value was produced.
    AUTO = calculated automatically from qty * emission factor (our default MVP behavior).
    MANUAL = entered directly by a user (used when the auto-calc setting is off).
    """
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class ComplianceIssueStatus(str, Enum):
    """
    Open issues that pass their due_date get flagged as Overdue by a simple
    "compute on read" check (no scheduled job needed for the MVP).
    """
    OPEN = "Open"
    RESOLVED = "Resolved"
    OVERDUE = "Overdue"


class NotificationType(str, Enum):
    """
    The four notification triggers required by the business rules:
    new compliance issue, CSR/Challenge approval decisions,
    policy acknowledgement reminders, and badge unlocks.
    """
    COMPLIANCE_ISSUE_RAISED = "COMPLIANCE_ISSUE_RAISED"
    APPROVAL_DECISION = "APPROVAL_DECISION"
    POLICY_ACKNOWLEDGEMENT_REMINDER = "POLICY_ACKNOWLEDGEMENT_REMINDER"
    BADGE_UNLOCKED = "BADGE_UNLOCKED"


class GenericStatus(str, Enum):
    """
    Simple active/inactive status for master data records that don't need
    a more complex lifecycle (Department, Category, EmissionFactor, Policy,
    Badge, Reward, CsrActivity).
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"