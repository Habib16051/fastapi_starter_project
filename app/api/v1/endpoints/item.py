from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.item import ItemCreate, ItemRead
from app.crud import item as item_crud
from app.core.security import get_db, get_current_user
from app.db.models.user import User

router = APIRouter()

@router.post("/", response_model=ItemRead)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return item_crud.create_item(db=db, item=item)

@router.get("/", response_model=List[ItemRead])
def list_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return item_crud.get_items(db=db)
