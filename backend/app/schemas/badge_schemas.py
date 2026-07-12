from typing import Any, Optional

from pydantic import BaseModel


class BadgeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    unlock_rule: Optional[dict[str, Any]] = None
    icon_url: Optional[str] = None
