from typing import Optional

from sqlmodel import Session, select

from app.constants.enums import QuizStatus
from app.core.exceptions import NotFoundError
from app.models.quiz import Quiz


def list_quizzes(session: Session, status: Optional[QuizStatus] = None) -> list[Quiz]:
    query = select(Quiz)
    if status:
        query = query.where(Quiz.status == status)
    return list(session.exec(query).all())


def create_quiz(session: Session, data: dict) -> Quiz:
    quiz = Quiz(**data)
    session.add(quiz)
    session.commit()
    session.refresh(quiz)
    return quiz


def get_quiz(session: Session, quiz_id: int) -> Quiz:
    quiz = session.get(Quiz, quiz_id)
    if not quiz:
        raise NotFoundError("Quiz", quiz_id)
    return quiz


def update_quiz(session: Session, quiz_id: int, data: dict) -> Quiz:
    quiz = get_quiz(session, quiz_id)
    for key, value in data.items():
        if value is not None:
            setattr(quiz, key, value)
    session.add(quiz)
    session.commit()
    session.refresh(quiz)
    return quiz


def delete_quiz(session: Session, quiz_id: int) -> None:
    quiz = get_quiz(session, quiz_id)
    session.delete(quiz)
    session.commit()
