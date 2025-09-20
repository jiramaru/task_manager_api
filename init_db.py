from app.database import engine, Base
from app import models
from app.models import user, task  # imports both models to register with the Base

# Create all difined tables from models.py
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
