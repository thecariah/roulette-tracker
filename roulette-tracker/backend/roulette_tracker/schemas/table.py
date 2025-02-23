from pydantic import BaseModel
from datetime import datetime

# Base schema for table
class TableBase(BaseModel):
    name: str

# Schema for creating a new table
class TableCreate(TableBase):
    pass

# Schema for responding with table data
class TableResponse(TableBase):
    id_table: int
    created: datetime
    last_save: datetime

    class Config:
        from_attributes = True
