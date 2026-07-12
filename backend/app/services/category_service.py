from typing import Optional

from sqlmodel import Session, select

from app.constants.enums import CategoryType
from app.core.exceptions import NotFoundError
from app.models.category import Category


def list_categories(session: Session, category_type: Optional[CategoryType] = None) -> list[Category]:
    query = select(Category)
    if category_type:
        query = query.where(Category.type == category_type)
    return list(session.exec(query).all())


def create_category(session: Session, data: dict) -> Category:
    category = Category(**data)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_category(session: Session, category_id: int) -> Category:
    category = session.get(Category, category_id)
    if not category:
        raise NotFoundError("Category", category_id)
    return category
