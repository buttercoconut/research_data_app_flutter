from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas import ResearchDataCreate, ResearchData as ResearchDataModel
from schemas import ResearchDataCreate as ResearchDataCreateSchema, ResearchData as ResearchDataSchema

router = APIRouter()

@router.get("/", response_model=List[ResearchDataSchema])
async def read_research_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(ResearchDataModel).offset(skip).limit(limit).all()

@router.post("/", response_model=ResearchDataSchema)
async def create_research_data(data: ResearchDataCreate, db: Session = Depends(get_db)):
    db_data = ResearchDataModel(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
