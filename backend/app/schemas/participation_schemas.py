from typing import Optional

from pydantic import BaseModel

from app.constants.enums import ApprovalStatus


class ParticipationJoin(BaseModel):
    proof_url: Optional[str] = None


class ParticipationApprove(BaseModel):
    approval_status: ApprovalStatus
    points_earned: Optional[int] = None
