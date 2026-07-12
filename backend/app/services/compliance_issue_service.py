from datetime import date
from typing import Optional

from sqlmodel import Session, select

from app.constants.enums import ComplianceIssueStatus, NotificationType
from app.core.exceptions import NotFoundError
from app.models.compliance_issue import ComplianceIssue
from app.notifications.service import create_notification


def _apply_overdue_flag(issue: ComplianceIssue) -> ComplianceIssue:
    if (
        issue.status == ComplianceIssueStatus.OPEN
        and issue.due_date
        and issue.due_date < date.today()
    ):
        issue.status = ComplianceIssueStatus.OVERDUE
    return issue


def list_compliance_issues(
    session: Session,
    status: Optional[ComplianceIssueStatus] = None,
    overdue: bool = False,
) -> list[ComplianceIssue]:
    issues = list(session.exec(select(ComplianceIssue)).all())
    for issue in issues:
        _apply_overdue_flag(issue)

    if status:
        issues = [i for i in issues if i.status == status]
    if overdue:
        issues = [i for i in issues if i.status == ComplianceIssueStatus.OVERDUE]
    return issues


def create_compliance_issue(session: Session, data: dict) -> ComplianceIssue:
    issue = ComplianceIssue(**data)
    session.add(issue)
    session.commit()
    session.refresh(issue)

    if issue.owner_employee_id:
        create_notification(
            session,
            employee_id=issue.owner_employee_id,
            notification_type=NotificationType.COMPLIANCE_ISSUE_RAISED,
            title="New Compliance Issue",
            message=issue.description or "A new compliance issue has been assigned to you.",
        )

    return issue


def update_compliance_issue(session: Session, issue_id: int, data: dict) -> ComplianceIssue:
    issue = session.get(ComplianceIssue, issue_id)
    if not issue:
        raise NotFoundError("ComplianceIssue", issue_id)

    for key, value in data.items():
        if value is not None:
            setattr(issue, key, value)

    _apply_overdue_flag(issue)
    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue
