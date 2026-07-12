from decimal import Decimal
from typing import Optional


def calculate_department_scores(
    *,
    total_co2e_kg: Decimal,
    approved_csr_count: int,
    approved_challenge_count: int,
    policy_ack_rate: float,
    open_compliance_count: int,
    overdue_compliance_count: int,
) -> dict[str, Decimal]:
    """Pure scoring function — environmental lower carbon is better, social/governance higher is better."""
    environmental = max(Decimal("0"), Decimal("100") - min(total_co2e_kg / Decimal("10"), Decimal("100")))

    social = Decimal(min(100, approved_csr_count * 10 + approved_challenge_count * 5))

    governance_base = Decimal(str(round(policy_ack_rate * 100, 2)))
    governance_penalty = Decimal(open_compliance_count * 5 + overdue_compliance_count * 10)
    governance = max(Decimal("0"), governance_base - governance_penalty)

    total = (environmental * Decimal("0.4")) + (social * Decimal("0.3")) + (governance * Decimal("0.3"))

    return {
        "environmental_score": round(environmental, 2),
        "social_score": round(social, 2),
        "governance_score": round(governance, 2),
        "total_score": round(total, 2),
    }


def calculate_org_score(
    department_scores: list[Decimal],
    weights: Optional[tuple[int, int, int]] = None,
) -> Decimal:
    """Weighted average of department total scores."""
    if not department_scores:
        return Decimal("0.00")
    return round(sum(department_scores) / len(department_scores), 2)
