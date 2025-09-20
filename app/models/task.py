from uuid import uuid4
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(Integer, default=1)  # low, medium, high
    completed = Column(Boolean, default=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # user.id foreign key
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    # relation with the owner
    owner = relationship("User", back_populates="tasks")
