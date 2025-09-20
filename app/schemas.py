from typing import Optional, List
from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr


# USER SCHEMAS
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # plain password, only for creation


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True  # allows reading data from ORM objects


# TASK SCHEMAS
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: int = 1
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None


class TaskRead(TaskBase):
    id: uuid.UUID
    created_at: datetime
    owner_id: uuid.UUID

    class Config:
        orm_mode = True


# NESTED RELATIONS


# task with owner info inside
class TaskReadWithOwner(TaskRead):
    owner: UserRead


# User with task inside
class UserReadWithTasks(UserRead):
    tasks: List[TaskRead] = []
