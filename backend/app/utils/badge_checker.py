from typing import Any, Optional

from sqlmodel import Session, select

from app.models.badge import Badge, EmployeeBadge
from app.models.challenge_participation import ChallengeParticipation
from app.models.user import User
from app.constants.enums import ApprovalStatus


def _rule_satisfied(rule: dict[str, Any], *, xp: int, completed_challenges: int) -> bool:
    rule_type = rule.get("type")
    threshold = rule.get("threshold", 0)

    if rule_type == "xp":
        return xp >= threshold
    if rule_type == "completed_challenges":
        return completed_challenges >= threshold
    return False


def check_and_award_badges(session: Session, employee_id: int, auto_award: bool = True) -> list[Badge]:
    """Evaluate unlock rules and award any newly earned badges."""
    if not auto_award:
        return []

    user = session.get(User, employee_id)
    if not user:
        return []

    completed = session.exec(
        select(ChallengeParticipation).where(
            ChallengeParticipation.employee_id == employee_id,
            ChallengeParticipation.approval_status == ApprovalStatus.APPROVED,
        )
    ).all()
    completed_count = len(completed)

    existing_ids = {
        eb.badge_id
        for eb in session.exec(
            select(EmployeeBadge).where(EmployeeBadge.employee_id == employee_id)
        ).all()
    }

    awarded: list[Badge] = []
    badges = session.exec(select(Badge).where(Badge.status == "Active")).all()

    for badge in badges:
        if badge.id in existing_ids or not badge.unlock_rule:
            continue
        if _rule_satisfied(badge.unlock_rule, xp=user.xp_points, completed_challenges=completed_count):
            session.add(EmployeeBadge(employee_id=employee_id, badge_id=badge.id))
            awarded.append(badge)

    if awarded:
        session.commit()

    return awarded
