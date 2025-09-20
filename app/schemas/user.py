from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional, List
from app.schemas.task import TaskRead


# Base schema (shared fields)
class UserBase(BaseModel):

    username: str
    email: EmailStr


# Schema for creating a user (requires password)
class UserCreate(UserBase):

    password: str


# Schema for updating a user (all fields optional)
class UserUpdate(BaseModel):

    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# Schema returned to the client (Read Model)
class UserRead(UserBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True  # allows reading from SQLAlchemy models


# For including related tasks (if need)
class UserWithTasks(UserRead):
    # a forward ref, will be linked later
    tasks: List[TaskRead] = []
