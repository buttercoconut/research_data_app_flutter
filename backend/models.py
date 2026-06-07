from sqlalchemy import Column, Integer, String
from database import Base

class ResearchData(Base):
    __tablename__ = "research_data"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    sample_size = Column(Integer)
    field = Column(String)
    field_name = Column(String)
