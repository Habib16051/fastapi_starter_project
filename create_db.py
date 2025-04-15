from app.db.session import engine
from app.db.base import Base  # ✅ Base that imports ALL models

def init_db():
    # ⚠️ Warning: DO NOT use this in production!
    # Alembic should be used for managing schema migrations.
    print("⚠️ This is a dev-only script. Alembic now manages your schema.")
    Base.metadata.create_all(bind=engine)  # Use only for testing or CI pipelines

if __name__ == "__main__":
    init_db()
