from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    fake_hashed_pw = "notreallyhashed_" + user.password
    db_user = User(
        email=user.email,
        hashed_password=fake_hashed_pw,
        full_name=user.full_name,
        is_active=1
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
