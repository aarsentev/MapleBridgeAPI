from pydantic import BaseModel
from typing import Optional
import datetime


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    dob: Optional[datetime.date] = None
    immigration_reason: Optional[bool] = None
    institution: Optional[str] = None
    interests: Optional[str] = None
    address: Optional[str] = None


class User(UserBase):
    user_id: int
    dob: Optional[datetime.date] = None
    immigration_reason: Optional[bool] = None
    institution: Optional[str] = None
    interests: Optional[str] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True
