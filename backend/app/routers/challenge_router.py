from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.constants.enums import ChallengeStatus
from app.database import get_session
from app.dependencies import get_current_user
from app.models.challenge import Challenge
from app.models.challenge_participation import ChallengeParticipation
from app.models.user import User
from app.schemas.challenge_schemas import ChallengeParticipationJoin, ChallengeStatusUpdate
from app.services import challenge_participation_service, challenge_service

router = APIRouter(prefix="/challenges", tags=["Challenges"])


@router.get("", response_model=list[Challenge])
def list_challenges(
    status: Optional[ChallengeStatus] = Query(default=None),
    session: Session = Depends(get_session),
):
    return challenge_service.list_challenges(session, status)


@router.post("", response_model=Challenge)
def create_challenge(data: Challenge, session: Session = Depends(get_session)):
    return challenge_service.create_challenge(session, data.model_dump(exclude={"id", "created_at"}))


@router.patch("/{challenge_id}/status", response_model=Challenge)
def update_status(
    challenge_id: int,
    payload: ChallengeStatusUpdate,
    session: Session = Depends(get_session),
):
    return challenge_service.update_challenge_status(session, challenge_id, payload.status)


@router.post("/{challenge_id}/join", response_model=ChallengeParticipation)
def join_challenge(
    challenge_id: int,
    payload: ChallengeParticipationJoin | None = None,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    data = payload or ChallengeParticipationJoin()
    return challenge_participation_service.join_challenge(
        session, challenge_id, current_user, data
    )
