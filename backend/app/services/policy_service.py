from datetime import datetime

from sqlmodel import Session, select

from app.constants.enums import AcknowledgementStatus
from app.core.exceptions import NotFoundError
from app.models.policy import Policy, PolicyAcknowledgement
from app.models.user import User


def list_policies(session: Session) -> list[Policy]:
    return list(session.exec(select(Policy)).all())


def create_policy(session: Session, data: dict) -> Policy:
    policy = Policy(**data)
    session.add(policy)
    session.commit()
    session.refresh(policy)
    return policy


def acknowledge_policy(session: Session, policy_id: int, user: User) -> PolicyAcknowledgement:
    policy = session.get(Policy, policy_id)
    if not policy:
        raise NotFoundError("Policy", policy_id)

    existing = session.exec(
        select(PolicyAcknowledgement).where(
            PolicyAcknowledgement.policy_id == policy_id,
            PolicyAcknowledgement.employee_id == user.id,
        )
    ).first()

    if existing:
        existing.status = AcknowledgementStatus.ACKNOWLEDGED
        existing.acknowledged_at = datetime.utcnow()
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing

    ack = PolicyAcknowledgement(
        policy_id=policy_id,
        employee_id=user.id,
        status=AcknowledgementStatus.ACKNOWLEDGED,
        acknowledged_at=datetime.utcnow(),
    )
    session.add(ack)
    session.commit()
    session.refresh(ack)
    return ack
