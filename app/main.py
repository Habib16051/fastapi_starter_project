from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.api.v1.endpoints import auth
from app.api.v1.endpoints import item

app = FastAPI(title="FastAPI Starter 🚀", version="1.0.0")

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(item.router, prefix="/api/v1/items", tags=["Items"])


@app.get("/")
def root():
    return {"message": "🚀 Welcome to FastAPI Starter Project!"}
