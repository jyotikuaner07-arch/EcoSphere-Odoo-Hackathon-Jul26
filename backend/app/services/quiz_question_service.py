from typing import Optional

from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.quiz import QuizQuestion, Quiz


def list_quiz_questions(session: Session, quiz_id: Optional[int] = None) -> list[QuizQuestion]:
    query = select(QuizQuestion)
    if quiz_id:
        query = query.where(QuizQuestion.quiz_id == quiz_id)
    return list(session.exec(query).all())


def create_quiz_question(session: Session, quiz_id: int, data: dict) -> QuizQuestion:
    # Verify quiz exists
    quiz = session.get(Quiz, quiz_id)
    if not quiz:
        raise NotFoundError("Quiz", quiz_id)
    question = QuizQuestion(quiz_id=quiz_id, **data)
    session.add(question)
    session.commit()
    session.refresh(question)
    return question


def get_quiz_question(session: Session, question_id: int) -> QuizQuestion:
    question = session.get(QuizQuestion, question_id)
    if not question:
        raise NotFoundError("Quiz Question", question_id)
    return question


def update_quiz_question(session: Session, question_id: int, data: dict) -> QuizQuestion:
    question = get_quiz_question(session, question_id)
    for key, value in data.items():
        if value is not None:
            setattr(question, key, value)
    session.add(question)
    session.commit()
    session.refresh(question)
    return question


def delete_quiz_question(session: Session, question_id: int) -> None:
    question = get_quiz_question(session, question_id)
    session.delete(question)
    session.commit()
