# app/crud/auth.py
from sqlalchemy.orm import Session
from app.crud.user import get_user_by_email
from app.core.security import verify_password
from app.db.models.user import User

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
