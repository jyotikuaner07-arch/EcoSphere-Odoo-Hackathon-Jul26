from typing import Optional

from sqlmodel import Session, select

from app.constants.enums import ChallengeStatus
from app.core.exceptions import NotFoundError
from app.models.challenge import Challenge


def list_challenges(session: Session, status: Optional[ChallengeStatus] = None) -> list[Challenge]:
    query = select(Challenge)
    if status:
        query = query.where(Challenge.status == status)
    return list(session.exec(query).all())


def create_challenge(session: Session, data: dict) -> Challenge:
    challenge = Challenge(**data)
    session.add(challenge)
    session.commit()
    session.refresh(challenge)
    return challenge


def get_challenge(session: Session, challenge_id: int) -> Challenge:
    challenge = session.get(Challenge, challenge_id)
    if not challenge:
        raise NotFoundError("Challenge", challenge_id)
    return challenge


def update_challenge_status(session: Session, challenge_id: int, status: ChallengeStatus) -> Challenge:
    challenge = get_challenge(session, challenge_id)
    challenge.status = status
    session.add(challenge)
    session.commit()
    session.refresh(challenge)
    return challenge
