from datetime import datetime
from typing import Optional

from sqlmodel import Session, select

from app.constants.enums import QuizStatus
from app.core.exceptions import NotFoundError, BadRequestError
from app.models.quiz import Quiz, QuizQuestion, QuizParticipation
from app.models.user import User
from app.schemas.quiz_schemas import QuizAnswer


def list_quiz_participations(
    session: Session,
    quiz_id: Optional[int] = None,
    employee_id: Optional[int] = None,
) -> list[QuizParticipation]:
    query = select(QuizParticipation)
    if quiz_id:
        query = query.where(QuizParticipation.quiz_id == quiz_id)
    if employee_id:
        query = query.where(QuizParticipation.employee_id == employee_id)
    return list(session.exec(query).all())


def get_quiz_participation(session: Session, participation_id: int) -> QuizParticipation:
    participation = session.get(QuizParticipation, participation_id)
    if not participation:
        raise NotFoundError("Quiz Participation", participation_id)
    return participation


def start_quiz_participation(session: Session, quiz_id: int, employee_id: int) -> QuizParticipation:
    quiz = session.get(Quiz, quiz_id)
    if not quiz:
        raise NotFoundError("Quiz", quiz_id)
    if quiz.status != QuizStatus.ACTIVE:
        raise BadRequestError("Quiz is not active")

    employee = session.get(User, employee_id)
    if not employee:
        raise NotFoundError("Employee", employee_id)

    participation = QuizParticipation(quiz_id=quiz_id, employee_id=employee_id)
    session.add(participation)
    session.commit()
    session.refresh(participation)
    return participation


def submit_quiz(session: Session, participation_id: int, answers: list[QuizAnswer]) -> QuizParticipation:
    participation = get_quiz_participation(session, participation_id)
    if participation.completed_at:
        raise BadRequestError("Quiz already submitted")

    quiz = session.get(Quiz, participation.quiz_id)
    questions = session.exec(select(QuizQuestion).where(QuizQuestion.quiz_id == quiz.id)).all()
    question_map = {q.id: q for q in questions}

    score = 0
    for answer in answers:
        question = question_map.get(answer.question_id)
        if question and answer.selected_option.upper() == question.correct_option.upper():
            score += 1

    participation.score = score
    xp_awarded = quiz.xp if score == len(questions) else (quiz.xp // 2 if score >= len(questions) // 2 else 0)
    participation.xp_awarded = xp_awarded
    participation.completed_at = datetime.utcnow()

    # Award XP to employee
    employee = session.get(User, participation.employee_id)
    employee.xp_points += xp_awarded

    session.add(participation)
    session.add(employee)
    session.commit()
    session.refresh(participation)

    return participation
