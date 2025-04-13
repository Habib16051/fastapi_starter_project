from fastapi import FastAPI
from app.api.v1.endpoints import user

app = FastAPI(title="FastAPI Starter 🚀", version="1.0.0")

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "🚀 Welcome to FastAPI Starter Project!"}
