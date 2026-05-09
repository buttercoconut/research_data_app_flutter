"""CRUD operations for ResearchData.

These functions are used by the router to interact with the database.
"""

from typing import List, Optional

from sqlmodel import Session, select

from .models import ResearchData, ResearchDataCreate, ResearchDataUpdate

# Create

def create_research_data(db: Session, data: ResearchDataCreate) -> ResearchData:
    db_data = ResearchData.from_orm(data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

# Read all

def get_all_research_data(db: Session, skip: int = 0, limit: int = 100) -> List[ResearchData]:
    statement = select(ResearchData).offset(skip).limit(limit)
    results = db.exec(statement).all()
    return results

# Read one

def get_research_data(db: Session, data_id: int) -> Optional[ResearchData]:
    return db.get(ResearchData, data_id)

# Update

def update_research_data(db: Session, data_id: int, data: ResearchDataUpdate) -> Optional[ResearchData]:
    db_data = db.get(ResearchData, data_id)
    if not db_data:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_data, key, value)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

# Delete

def delete_research_data(db: Session, data_id: int) -> bool:
    db_data = db.get(ResearchData, data_id)
    if not db_data:
        return False
    db.delete(db_data)
    db.commit()
    return True
