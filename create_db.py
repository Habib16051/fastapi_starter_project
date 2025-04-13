# create_db.py
from app.db.session import engine
from app.db.base import Base  # ✅ Base that imports ALL models

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database schema created!")

if __name__ == "__main__":
    init_db()
