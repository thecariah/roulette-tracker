from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from roulette_tracker.crud.table import get_tables, create_table
from roulette_tracker.schemas.table import TableCreate, TableResponse
from roulette_tracker.dependencies import get_db

router = APIRouter()

@router.get("/tables/", response_model=list[TableResponse])
def read_tables(db: Session = Depends(get_db)):
    return get_tables(db)

@router.post("/tables/", response_model=TableResponse)
def add_table(table: TableCreate, db: Session = Depends(get_db)):
    return create_table(db, table)
