from .database import SessionLocal
from sqlalchemy.orm import Session

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
