from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

class ShortURL(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, nullable=False)
    long_url = Column(String, nullable=False)
    visit_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime, nullable=True)