from uuid import UUID
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


# Create Task
def create_task(db: Session, task: TaskCreate, owner_id: UUID) -> Task:
    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        completed=task.completed,
        due_date=task.due_date,
        owner_id=owner_id,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


# Get all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 10) -> List[Task]:
    return db.query(Task).offset(skip).limit(limit).all()


# get a single task by ID
def get_task(db: Session, task_id: UUID) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()


# get tasks by User
def get_tasks_by_user(db: Session, owner_id: UUID) -> List[Task]:
    return db.query(Task).filter(Task.owner_id == owner_id).all()


# Update Task
def update_task(db: Session, task_id: UUID, task_update: TaskUpdate) -> Optional[Task]:
    db_task = get_task(db, task_id)

    if not db_task:
        return None

    if task_update.title is not None:
        db_task.title = task_update.title
    if task_update.description is not None:
        db_task.description = task_update.description
    if task_update.completed is not None:
        db_task.completed = task_update.completed
    if task_update.priority is not None:
        db_task.priority = task_update.priority
    if task_update.due_date is not None:
        db_task.due_date = task_update.due_date

    db.commit()
    db.refresh(db_task)

    return db_task


# Delete a Task
def delete_task(db: Session, task_id: UUID) -> bool:
    db_task = get_task(db, task_id)

    if not db_task:
        return False

    db.delete(db_task)
    db.commit()

    return True
