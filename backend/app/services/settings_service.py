from sqlmodel import Session, select

from app.models.settings import OrganizationSettings


def get_or_create_settings(session: Session) -> OrganizationSettings:
    settings = session.get(OrganizationSettings, 1)
    if not settings:
        settings = OrganizationSettings(id=1)
        session.add(settings)
        session.commit()
        session.refresh(settings)
    return settings
