from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.constants.enums import ApprovalStatus


class ChallengeParticipation(SQLModel, table=True):
    __tablename__ = "challenge_participation"

    id: Optional[int] = Field(default=None, primary_key=True)
    challenge_id: int = Field(foreign_key="challenge.id")
    employee_id: int = Field(foreign_key="employees.id")
    progress: int = Field(default=0)
    proof_url: Optional[str] = Field(default=None, max_length=500)
    approval_status: ApprovalStatus = Field(default=ApprovalStatus.PENDING)
    xp_awarded: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
