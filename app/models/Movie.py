from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    type = Column(String(100))
    title = Column(String(100), nullable=False)
    director = Column(String(100))
    country = Column(String(100))
    release_year = Column(Integer, nullable=False)
    rating = Column(String(55))
    duration = Column(String(55))
    description = Column(String(255))

    reviews = relationship('Review', cascade='all,delete')
