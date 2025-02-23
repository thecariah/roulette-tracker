from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from roulette_tracker.database import Base

class Table(Base):
    # Table name
    __tablename__ = "tables"

    # Columns
    id_table = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created = Column(DateTime, default=datetime.now)
    last_save = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # Relationships
    numbers = relationship("Number", back_populates="table")
    croupiers = relationship("Table_Croupier", back_populates="table")
