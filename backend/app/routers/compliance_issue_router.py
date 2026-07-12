from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.constants.enums import ComplianceIssueStatus
from app.database import get_session
from app.models.compliance_issue import ComplianceIssue
from app.services import compliance_issue_service

router = APIRouter(prefix="/compliance-issues", tags=["Compliance Issues"])


@router.get("", response_model=list[ComplianceIssue])
def list_issues(
    status: Optional[ComplianceIssueStatus] = Query(default=None),
    overdue: bool = Query(default=False),
    session: Session = Depends(get_session),
):
    return compliance_issue_service.list_compliance_issues(session, status, overdue)


@router.get("/{issue_id}", response_model=ComplianceIssue)
def get_issue(issue_id: int, session: Session = Depends(get_session)):
    from app.core.exceptions import NotFoundError

    issues = compliance_issue_service.list_compliance_issues(session)
    for issue in issues:
        if issue.id == issue_id:
            return issue
    raise NotFoundError("ComplianceIssue", issue_id)


@router.post("", response_model=ComplianceIssue)
def create_issue(data: ComplianceIssue, session: Session = Depends(get_session)):
    return compliance_issue_service.create_compliance_issue(
        session, data.model_dump(exclude={"id", "raised_at"})
    )


@router.put("/{issue_id}", response_model=ComplianceIssue)
def update_issue(
    issue_id: int,
    data: ComplianceIssue,
    session: Session = Depends(get_session),
):
    return compliance_issue_service.update_compliance_issue(
        session,
        issue_id,
        data.model_dump(exclude={"id", "raised_at"}, exclude_unset=True),
    )
