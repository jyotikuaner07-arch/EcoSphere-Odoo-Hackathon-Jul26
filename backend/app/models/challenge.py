from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import ChallengeDifficulty, ChallengeStatus


class Challenge(SQLModel, table=True):
    __tablename__ = "challenge"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200)
    category_id: int = Field(foreign_key="categories.id")
    description: Optional[str] = None
    xp: int = Field(default=0)
    difficulty: ChallengeDifficulty = Field(default=ChallengeDifficulty.EASY)
    evidence_required: bool = Field(default=False)
    deadline: Optional[date] = None
    status: ChallengeStatus = Field(default=ChallengeStatus.DRAFT)
    created_at: datetime = Field(default_factory=datetime.utcnow)
