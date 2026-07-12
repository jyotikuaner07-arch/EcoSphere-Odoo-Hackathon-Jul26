from typing import Callable

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.auth.jwt_handler import decode_access_token
from app.constants.enums import UserRole
from app.core.exceptions import InvalidCredentialsError, PermissionDeniedError
from app.database import get_session
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> User:
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise InvalidCredentialsError("Invalid or expired token.")

    user_id = int(payload["sub"])
    user = session.get(User, user_id)
    if not user:
        raise InvalidCredentialsError("User not found.")
    return user


def require_role(*roles: UserRole) -> Callable:
    def checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in roles:
            raise PermissionDeniedError()
        return current_user

    return checker
