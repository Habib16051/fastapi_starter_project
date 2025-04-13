from pydantic import BaseModel

class UserBase(BaseModel):
    email: str | None = None
    full_name: str | None = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
