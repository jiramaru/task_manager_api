from sqlalchemy import Column, ForeignKey, String, DateTime, Text, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        default=uuid4,
        primary_key=True,
        index=True,
        unique=True,
        nullable=True,
    )
    username = Column(String, index=True, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship: one user --) many tasks
    tesks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        UUID(as_uuid=True),
        default=uuid4,
        primary_key=True,
        index=True,
        unique=True,
        nullable=False,
    )

    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False)
    priority = Column(Integer, default=1)  # 1 = low; 2 = medium ; 3 = high
    due_date = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    # relationship back to the owner
    owner = relationship("User", back_populates="tasks")
