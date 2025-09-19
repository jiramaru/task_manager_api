from app.database import engine, Base
from app import models

# Create all difined tables from models.py
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
