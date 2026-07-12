from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.constants.enums import QuizStatus
from app.database import get_session
from app.dependencies import get_current_user
from app.models.quiz import Quiz, QuizQuestion, QuizParticipation
from app.models.user import User
from app.schemas.quiz_schemas import (
    QuizCreate,
    QuizUpdate,
    QuizQuestionCreate,
    QuizQuestionUpdate,
    QuizSubmit,
    QuizResponse,
    QuizQuestionResponse,
    QuizParticipationResponse,
)
from app.services import (
    quiz_service,
    quiz_question_service,
    quiz_participation_service,
)

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])


# Quiz Endpoints
@router.get("", response_model=list[QuizResponse])
def list_quizzes(
    status: Optional[QuizStatus] = Query(default=None),
    session: Session = Depends(get_session),
):
    return quiz_service.list_quizzes(session, status)


@router.post("", response_model=QuizResponse)
def create_quiz(data: QuizCreate, session: Session = Depends(get_session)):
    return quiz_service.create_quiz(session, data.model_dump())


@router.get("/{quiz_id}", response_model=QuizResponse)
def get_quiz(quiz_id: int, session: Session = Depends(get_session)):
    return quiz_service.get_quiz(session, quiz_id)


@router.patch("/{quiz_id}", response_model=QuizResponse)
def update_quiz(
    quiz_id: int, data: QuizUpdate, session: Session = Depends(get_session)
):
    return quiz_service.update_quiz(session, quiz_id, data.model_dump(exclude_unset=True))


@router.delete("/{quiz_id}")
def delete_quiz(quiz_id: int, session: Session = Depends(get_session)):
    quiz_service.delete_quiz(session, quiz_id)
    return {"detail": "Quiz deleted successfully"}


# Quiz Question Endpoints
@router.get("/{quiz_id}/questions", response_model=list[QuizQuestionResponse])
def list_quiz_questions(quiz_id: int, session: Session = Depends(get_session)):
    return quiz_question_service.list_quiz_questions(session, quiz_id)


@router.post("/{quiz_id}/questions", response_model=QuizQuestionResponse)
def create_quiz_question(
    quiz_id: int, data: QuizQuestionCreate, session: Session = Depends(get_session)
):
    return quiz_question_service.create_quiz_question(session, quiz_id, data.model_dump())


@router.get("/questions/{question_id}", response_model=QuizQuestionResponse)
def get_quiz_question(question_id: int, session: Session = Depends(get_session)):
    return quiz_question_service.get_quiz_question(session, question_id)


@router.patch("/questions/{question_id}", response_model=QuizQuestionResponse)
def update_quiz_question(
    question_id: int, data: QuizQuestionUpdate, session: Session = Depends(get_session)
):
    return quiz_question_service.update_quiz_question(
        session, question_id, data.model_dump(exclude_unset=True)
    )


@router.delete("/questions/{question_id}")
def delete_quiz_question(question_id: int, session: Session = Depends(get_session)):
    quiz_question_service.delete_quiz_question(session, question_id)
    return {"detail": "Question deleted successfully"}


# Quiz Participation Endpoints
@router.get("/{quiz_id}/participations", response_model=list[QuizParticipationResponse])
def list_quiz_participations(
    quiz_id: int,
    employee_id: Optional[int] = Query(default=None),
    session: Session = Depends(get_session),
):
    return quiz_participation_service.list_quiz_participations(
        session, quiz_id, employee_id
    )


@router.post("/{quiz_id}/start", response_model=QuizParticipationResponse)
def start_quiz(
    quiz_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return quiz_participation_service.start_quiz_participation(
        session, quiz_id, current_user.id
    )


@router.post("/participations/{participation_id}/submit", response_model=QuizParticipationResponse)
def submit_quiz(
    participation_id: int,
    data: QuizSubmit,
    session: Session = Depends(get_session),
):
    return quiz_participation_service.submit_quiz(
        session, participation_id, data.answers
    )


@router.get("/participations/{participation_id}", response_model=QuizParticipationResponse)
def get_quiz_participation(
    participation_id: int, session: Session = Depends(get_session)
):
    return quiz_participation_service.get_quiz_participation(session, participation_id)
