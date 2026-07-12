from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.emission_factor import EmissionFactor


def list_emission_factors(session: Session) -> list[EmissionFactor]:
    return list(session.exec(select(EmissionFactor)).all())


def create_emission_factor(session: Session, data: dict) -> EmissionFactor:
    factor = EmissionFactor(**data)
    session.add(factor)
    session.commit()
    session.refresh(factor)
    return factor


def get_emission_factor(session: Session, factor_id: int) -> EmissionFactor:
    factor = session.get(EmissionFactor, factor_id)
    if not factor:
        raise NotFoundError("EmissionFactor", factor_id)
    return factor


def update_emission_factor(session: Session, factor_id: int, data: dict) -> EmissionFactor:
    factor = get_emission_factor(session, factor_id)
    for key, value in data.items():
        if value is not None:
            setattr(factor, key, value)
    session.add(factor)
    session.commit()
    session.refresh(factor)
    return factor
