from typing import Optional

from pydantic import BaseModel

from app.constants.enums import ApprovalStatus, ChallengeStatus


class ChallengeStatusUpdate(BaseModel):
    status: ChallengeStatus


class ChallengeParticipationJoin(BaseModel):
    proof_url: Optional[str] = None


class ChallengeParticipationProgress(BaseModel):
    progress: int
    proof_url: Optional[str] = None


class ChallengeParticipationApprove(BaseModel):
    approval_status: ApprovalStatus
