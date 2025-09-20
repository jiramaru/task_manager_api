from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

# for nested relations
from app.schemas.user import UserRead


# Base Schema shared by creation/update
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int = 1
    completed: bool = False
    due_date: Optional[datetime] = None


# Schema for creating a task
class TaskCreate(TaskBase):
    pass  # Inherits all fields from TaskBase


# Schema for updating a task (All fields optional)
class TaskUpdate(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None


# Schema returned to the client
class TaskRead(TaskBase):
    id: UUID
    owner_id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# task with nested owner info
class TaskWithOwner(TaskRead):
    owner: UserRead
