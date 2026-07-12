from typing import Optional

from pydantic import BaseModel, EmailStr

from app.constants.enums import UserRole


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    department_id: int
    role: UserRole = UserRole.EMPLOYEE


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    department_id: int
    xp_points: int

    model_config = {"from_attributes": True}
