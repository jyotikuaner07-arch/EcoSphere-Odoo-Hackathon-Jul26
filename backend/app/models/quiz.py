from datetime import datetime, date
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import QuizStatus, QuizDifficulty


class Quiz(SQLModel, table=True):
    __tablename__ = "quiz"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200)
    category_id: int = Field(foreign_key="categories.id")
    description: Optional[str] = None
    xp: int = Field(default=0)
    difficulty: QuizDifficulty = Field(default=QuizDifficulty.EASY)
    deadline: Optional[date] = None
    status: QuizStatus = Field(default=QuizStatus.DRAFT)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class QuizQuestion(SQLModel, table=True):
    __tablename__ = "quiz_question"

    id: Optional[int] = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quiz.id")
    question_text: str = Field(max_length=500)
    option_a: str = Field(max_length=200)
    option_b: str = Field(max_length=200)
    option_c: str = Field(max_length=200)
    option_d: str = Field(max_length=200)
    correct_option: str = Field(max_length=1)  # "A", "B", "C", "D"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class QuizParticipation(SQLModel, table=True):
    __tablename__ = "quiz_participation"

    id: Optional[int] = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quiz.id")
    employee_id: int = Field(foreign_key="employees.id")
    score: int = Field(default=0)
    xp_awarded: int = Field(default=0)
    completed_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
