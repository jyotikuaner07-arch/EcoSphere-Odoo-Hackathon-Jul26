from sqlmodel import Session, select, func

from app.constants.enums import ApprovalStatus, ChallengeStatus, ComplianceIssueStatus
from app.models.challenge import Challenge
from app.models.challenge_participation import ChallengeParticipation
from app.models.compliance_issue import ComplianceIssue
from app.models.csr_activity import CsrActivity
from app.models.participation import Participation
from app.models.user import User
from app.services.scoring_service import calculate_organization_score
from app.reports.service import build_report_summary


def get_dashboard_summary(session: Session) -> dict:
    org_score = calculate_organization_score(session)

    total_csr = session.exec(select(func.count(CsrActivity.id))).one()
    pending_participations = session.exec(
        select(func.count(Participation.id)).where(
            Participation.approval_status == ApprovalStatus.PENDING
        )
    ).one()
    active_challenges = session.exec(
        select(func.count(Challenge.id)).where(Challenge.status == ChallengeStatus.ACTIVE)
    ).one()
    open_issues = session.exec(
        select(func.count(ComplianceIssue.id)).where(
            ComplianceIssue.status == ComplianceIssueStatus.OPEN
        )
    ).one()

    top_employees = session.exec(
        select(User).order_by(User.xp_points.desc()).limit(5)
    ).all()

    return {
        "organization_score": org_score,
        "kpis": {
            "total_csr_activities": int(total_csr),
            "pending_approvals": int(pending_participations),
            "active_challenges": int(active_challenges),
            "open_compliance_issues": int(open_issues),
        },
        "leaderboard_preview": [
            {"id": u.id, "name": u.name, "xp_points": u.xp_points} for u in top_employees
        ],
        "report_preview": build_report_summary(session),
    }


def get_leaderboard(
    session: Session,
    department_id: int | None = None,
    period: str | None = None,
) -> list[dict]:
    query = select(User).order_by(User.xp_points.desc())
    if department_id:
        query = query.where(User.department_id == department_id)
    users = session.exec(query.limit(20)).all()
    return [
        {
            "rank": idx + 1,
            "employee_id": u.id,
            "name": u.name,
            "department_id": u.department_id,
            "xp_points": u.xp_points,
            "period": period or "all-time",
        }
        for idx, u in enumerate(users)
    ]
