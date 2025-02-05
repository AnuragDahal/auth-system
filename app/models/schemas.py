from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponseModel(BaseModel):
    status: str
    message: str
    data: Optional[dict]
