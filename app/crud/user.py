from sqlalchemy.orm import Session
from app.utils.security import hash_password
from typing import Optional, List
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User
import uuid


# Create a new User
def create_user(db: Session, user: UserCreate) -> User:

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


# Get a User by id
def get_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


# Get a user by Email
def get_user_by_email(db: Session, user_email: str) -> Optional[User]:
    return db.query(User).filter(User.email == user_email).first()


# Update User
def update_user(
    db: Session, user_id: uuid.UUID, user_update: UserUpdate
) -> Optional[User]:
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    if user_update.username is not None:
        db_user.username = user_update.username
    if user_update.email is not None:
        db_user.email = user_update.email
    if user_update.password is not None:
        db_user.hashed_password = hash_password(user_update.password)

    db.commit()
    db.refresh(db_user)

    return db_user


# Delete User
def delete_user(db: Session, user_id: uuid.UUID) -> bool:
    db_user = get_user(db, user_id)

    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True
