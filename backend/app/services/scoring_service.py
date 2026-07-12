from decimal import Decimal

from sqlmodel import Session

from app.models.department_score import DepartmentScore
from app.reports.service import (
    get_department_carbon_total,
    get_governance_metrics,
    get_social_counts,
)
from app.services.department_service import get_department
from app.services.settings_service import get_or_create_settings
from app.utils.score_calculator import calculate_department_scores, calculate_org_score


def calculate_department_score(session: Session, department_id: int) -> dict:
    get_department(session, department_id)
    settings = get_or_create_settings(session)

    carbon = get_department_carbon_total(session, department_id)
    social = get_social_counts(session, department_id)
    gov = get_governance_metrics(session, department_id)

    scores = calculate_department_scores(
        total_co2e_kg=carbon,
        approved_csr_count=social["approved_csr"],
        approved_challenge_count=social["approved_challenges"],
        policy_ack_rate=gov["policy_ack_rate"],
        open_compliance_count=gov["open_issues"],
        overdue_compliance_count=gov["overdue_issues"],
    )

    env_w = settings.environmental_weight / 100
    social_w = settings.social_weight / 100
    gov_w = settings.governance_weight / 100
    total = (
        scores["environmental_score"] * Decimal(str(env_w))
        + scores["social_score"] * Decimal(str(social_w))
        + scores["governance_score"] * Decimal(str(gov_w))
    )
    scores["total_score"] = round(total, 2)

    record = DepartmentScore(
        department_id=department_id,
        environmental_score=scores["environmental_score"],
        social_score=scores["social_score"],
        governance_score=scores["governance_score"],
        total_score=scores["total_score"],
    )
    session.add(record)
    session.commit()

    return {"department_id": department_id, **scores}


def calculate_organization_score(session: Session) -> dict:
    from sqlmodel import select
    from app.models.department import Department

    departments = session.exec(select(Department)).all()
    dept_scores = []
    breakdown = []

    for dept in departments:
        if dept.id is None:
            continue
        result = calculate_department_score(session, dept.id)
        dept_scores.append(result["total_score"])
        breakdown.append(result)

    org_total = calculate_org_score(dept_scores)
    settings = get_or_create_settings(session)

    return {
        "organization_score": org_total,
        "weights": {
            "environmental": settings.environmental_weight,
            "social": settings.social_weight,
            "governance": settings.governance_weight,
        },
        "departments": breakdown,
    }
