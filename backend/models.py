"""Domain models for research data.

Using SQLModel (a thin wrapper around SQLAlchemy + Pydantic) for ORM and validation.
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

class ResearchDataBase(SQLModel):
    title: str
    description: Optional[str] = None
    collected_at: datetime
    researcher: str

class ResearchData(ResearchDataBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ResearchDataCreate(ResearchDataBase):
    pass

class ResearchDataRead(ResearchDataBase):
    id: int

class ResearchDataUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    collected_at: Optional[datetime] = None
    researcher: Optional[str] = None
