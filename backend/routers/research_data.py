"""API router for research data.

Provides CRUD endpoints that the Flutter frontend will consume.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from ..database import get_db
from ..models import (
    ResearchData,
    ResearchDataCreate,
    ResearchDataRead,
    ResearchDataUpdate,
)
from ..crud import (
    create_research_data,
    delete_research_data,
    get_all_research_data,
    get_research_data,
    update_research_data,
)

router = APIRouter()

@router.post("/research_data", response_model=ResearchDataRead, status_code=status.HTTP_201_CREATED)
async def create_data(data: ResearchDataCreate, db: Depends(get_db)):
    return create_research_data(db, data)

@router.get("/research_data", response_model=list[ResearchDataRead])
async def read_all(skip: int = 0, limit: int = 100, db: Depends(get_db)):
    return get_all_research_data(db, skip=skip, limit=limit)

@router.get("/research_data/{data_id}", response_model=ResearchDataRead)
async def read_one(data_id: int, db: Depends(get_db)):
    db_data = get_research_data(db, data_id)
    if not db_data:
        raise HTTPException(status_code=404, detail="Research data not found")
    return db_data

@router.put("/research_data/{data_id}", response_model=ResearchDataRead)
async def update_one(data_id: int, data: ResearchDataUpdate, db: Depends(get_db)):
    db_data = update_research_data(db, data_id, data)
    if not db_data:
        raise HTTPException(status_code=404, detail="Research data not found")
    return db_data

@router.delete("/research_data/{data_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(data_id: int, db: Depends(get_db)):
    success = delete_research_data(db, data_id)
    if not success:
        raise HTTPException(status_code=404, detail="Research data not found")
    return
