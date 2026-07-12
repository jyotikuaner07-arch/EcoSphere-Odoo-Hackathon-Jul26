from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel

from app.constants.enums import QuizStatus, QuizDifficulty


class QuizCreate(BaseModel):
    title: str
    category_id: int
    description: Optional[str] = None
    xp: int = 0
    difficulty: QuizDifficulty = QuizDifficulty.EASY
    deadline: Optional[date] = None


class QuizUpdate(BaseModel):
    title: Optional[str] = None
    category_id: Optional[int] = None
    description: Optional[str] = None
    xp: Optional[int] = None
    difficulty: Optional[QuizDifficulty] = None
    deadline: Optional[date] = None
    status: Optional[QuizStatus] = None


class QuizQuestionCreate(BaseModel):
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str


class QuizQuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_option: Optional[str] = None


class QuizAnswer(BaseModel):
    question_id: int
    selected_option: str


class QuizSubmit(BaseModel):
    answers: list[QuizAnswer]


class QuizParticipationResponse(BaseModel):
    id: int
    quiz_id: int
    employee_id: int
    score: int
    xp_awarded: int
    completed_at: Optional[datetime] = None
    created_at: datetime


class QuizResponse(BaseModel):
    id: int
    title: str
    category_id: int
    description: Optional[str] = None
    xp: int
    difficulty: QuizDifficulty
    deadline: Optional[date] = None
    status: QuizStatus
    created_at: datetime


class QuizQuestionResponse(BaseModel):
    id: int
    quiz_id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    # Don't include correct_option in public responses
    created_at: datetime
