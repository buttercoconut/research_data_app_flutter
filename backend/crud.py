from sqlalchemy.orm import Session
from models import ResearchData
from schemas import ResearchDataCreate


def get_research_data(db: Session, data_id: int):
    return db.query(ResearchData).filter(ResearchData.id == data_id).first()


def get_research_data_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ResearchData).offset(skip).limit(limit).all()


def create_research_data(db: Session, data: ResearchDataCreate):
    db_data = ResearchData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
