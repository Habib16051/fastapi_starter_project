from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.auth import Token
from app.core.security import create_access_token
from app.crud.auth import authenticate_user

router = APIRouter()


# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Route: Login + Token generation
@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
#
# from app.schemas.token import Token, LoginRequest
# from app.db.session import SessionLocal
# from app.crud.user import get_user_by_email
# from app.core.security import verify_password, create_access_token
#
# router = APIRouter()
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# @router.post("/login", response_model=Token)
# def login_for_access_token(request: LoginRequest, db: Session = Depends(get_db)):
#     user = get_user_by_email(db, request.email)
#     if not user or not verify_password(request.password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password"
#         )
#
#     access_token = create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}
