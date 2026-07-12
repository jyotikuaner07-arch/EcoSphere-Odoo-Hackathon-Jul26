from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.services import scoring_service

router = APIRouter(prefix="/organization", tags=["Scoring"])


@router.get("/score")
def organization_score(session: Session = Depends(get_session)):
    return scoring_service.calculate_organization_score(session)
