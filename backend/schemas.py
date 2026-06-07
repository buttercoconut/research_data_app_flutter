from pydantic import BaseModel
from typing import Optional

class ResearchDataBase(BaseModel):
    title: str
    description: Optional[str] = None
    sample_size: int
    field: str

class ResearchDataCreate(ResearchDataBase):
    pass

class ResearchData(ResearchDataBase):
    id: int

    class Config:
        orm_mode = True
