from sqlalchemy.orm import Session
from app.db.models.item import Item
from app.schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate) -> Item:
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()
