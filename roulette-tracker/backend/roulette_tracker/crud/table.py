from sqlalchemy.orm import Session
from roulette_tracker.models.table import Table
from roulette_tracker.schemas.table import TableCreate

# Get all tables
def get_tables(db: Session):
    return db.query(Table).all()

# Creates a new table
def create_table(db: Session, table: TableCreate):
    db_table = Table(name=table.name)
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table
