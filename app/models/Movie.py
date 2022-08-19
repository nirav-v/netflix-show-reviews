from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    release_year = Column(Integer, nullable=False)

    reviews = relationship('Review', cascade='all,delete')
