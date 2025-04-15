from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.item import ItemCreate, ItemRead
from app.crud import item as item_crud
from app.core.security import get_db, get_current_user
from app.db.models.user import User
from app.db.models.item import Item

router = APIRouter()

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return item_crud.create_item(db=db, item=item, user_id=current_user.id)

@router.get("/", response_model=List[ItemRead])
def list_my_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 🧠 Only return items owned by the current user
    return db.query(Item).filter(Item.user_id == current_user.id).all()
