from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.constants.enums import UserRole
from app.database import get_session
from app.dependencies import require_role
from app.models.emission_factor import EmissionFactor
from app.models.user import User
from app.services import emission_factor_service

router = APIRouter(prefix="/emission-factors", tags=["Emission Factors"])


@router.get("", response_model=list[EmissionFactor])
def list_factors(session: Session = Depends(get_session)):
    return emission_factor_service.list_emission_factors(session)


@router.post("", response_model=EmissionFactor)
def create_factor(
    data: EmissionFactor,
    session: Session = Depends(get_session),
    _: User = Depends(require_role(UserRole.ADMIN, UserRole.SUSTAINABILITY_OFFICER)),
):
    return emission_factor_service.create_emission_factor(
        session, data.model_dump(exclude={"id", "created_at"})
    )
