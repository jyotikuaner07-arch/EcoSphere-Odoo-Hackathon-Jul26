from sqlmodel import Session, select

from app.auth.jwt_handler import create_access_token
from app.auth.security import hash_password, verify_password
from app.core.exceptions import InvalidCredentialsError, NotFoundError
from app.models.user import User
from app.schemas.auth_schemas import UserCreate, UserLogin


def register_user(session: Session, payload: UserCreate) -> User:
    existing = session.exec(select(User).where(User.email == payload.email)).first()
    if existing:
        raise InvalidCredentialsError("Email already registered.")

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        department_id=payload.department_id,
        role=payload.role,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def login_user(session: Session, payload: UserLogin) -> dict:
    user = session.exec(select(User).where(User.email == payload.email)).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise InvalidCredentialsError()

    token = create_access_token({"sub": str(user.id), "role": user.role.value})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "department_id": user.department_id,
            "xp_points": user.xp_points,
        },
    }


def get_user(session: Session, user_id: int) -> User:
    user = session.get(User, user_id)
    if not user:
        raise NotFoundError("User", user_id)
    return user
