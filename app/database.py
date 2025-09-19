from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os


# Load environement variables from .env file
load_dotenv()

# Get the database url from .env
DOCKER_DATABASE_URL = os.getenv("DATABASE_URL")

# Create SqlAlchemy engine (the 'phone line' to the database)
engine = create_engine(DOCKER_DATABASE_URL)

# Create a factory for the database sessions (like opening a call each time we need to talk)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base class for our database models (we'll use this in models.py)
Base = declarative_base()


# Function to get a database session for our API requests


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
