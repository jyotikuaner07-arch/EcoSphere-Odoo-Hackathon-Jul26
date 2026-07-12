from datetime import date
from decimal import Decimal
from typing import Any, Optional

from sqlmodel import Session, select, func

from app.constants.enums import ApprovalStatus, ComplianceIssueStatus
from app.models.carbon_transaction import CarbonTransaction
from app.models.compliance_issue import ComplianceIssue
from app.models.csr_activity import CsrActivity
from app.models.participation import Participation
from app.models.challenge_participation import ChallengeParticipation
from app.models.policy import PolicyAcknowledgement
from app.models.department import Department
from app.models.user import User


def get_department_carbon_total(session: Session, department_id: int) -> Decimal:
    result = session.exec(
        select(func.coalesce(func.sum(CarbonTransaction.co2e_kg), 0)).where(
            CarbonTransaction.department_id == department_id
        )
    ).one()
    return Decimal(str(result))


def get_social_counts(session: Session, department_id: int) -> dict[str, int]:
    approved_csr = session.exec(
        select(func.count(Participation.id))
        .join(CsrActivity, Participation.activity_id == CsrActivity.id)
        .where(
            CsrActivity.department_id == department_id,
            Participation.approval_status == ApprovalStatus.APPROVED,
        )
    ).one()

    approved_challenges = session.exec(
        select(func.count(ChallengeParticipation.id))
        .join(User, ChallengeParticipation.employee_id == User.id)
        .where(
            User.department_id == department_id,
            ChallengeParticipation.approval_status == ApprovalStatus.APPROVED,
        )
    ).one()

    return {"approved_csr": int(approved_csr), "approved_challenges": int(approved_challenges)}


def get_governance_metrics(session: Session, department_id: int) -> dict[str, Any]:
    employees = session.exec(select(User).where(User.department_id == department_id)).all()
    employee_ids = [e.id for e in employees if e.id is not None]

    if not employee_ids:
        return {"policy_ack_rate": 0.0, "open_issues": 0, "overdue_issues": 0}

    acks = session.exec(
        select(PolicyAcknowledgement).where(PolicyAcknowledgement.employee_id.in_(employee_ids))
    ).all()
    ack_rate = (
        sum(1 for a in acks if a.status.value == "Acknowledged") / len(acks) if acks else 0.0
    )

    issues = session.exec(
        select(ComplianceIssue).where(ComplianceIssue.department_id == department_id)
    ).all()
    today = date.today()
    open_count = sum(1 for i in issues if i.status == ComplianceIssueStatus.OPEN)
    overdue = sum(
        1
        for i in issues
        if i.status == ComplianceIssueStatus.OPEN and i.due_date and i.due_date < today
    )

    return {"policy_ack_rate": ack_rate, "open_issues": open_count, "overdue_issues": overdue}


def build_report_summary(session: Session, department_id: Optional[int] = None) -> dict[str, Any]:
    dept_query = select(Department)
    if department_id:
        dept_query = dept_query.where(Department.id == department_id)
    departments = session.exec(dept_query).all()

    rows = []
    for dept in departments:
        if dept.id is None:
            continue
        carbon = get_department_carbon_total(session, dept.id)
        social = get_social_counts(session, dept.id)
        gov = get_governance_metrics(session, dept.id)
        rows.append(
            {
                "department_id": dept.id,
                "department_name": dept.name,
                "carbon_kg": float(carbon),
                **social,
                **gov,
            }
        )

    return {"departments": rows, "generated_at": date.today().isoformat()}
