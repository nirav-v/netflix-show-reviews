from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func, true
from sqlalchemy.orm import relationship, column_property


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    type = Column(String(100))
    title = Column(String(2000))
    director = Column(String(2000))
    cast = Column(String(2000))
    country = Column(String(100))
    date_added = Column(String(100))
    release_year = Column(Integer)
    rating = Column(String(55))
    duration = Column(String(55))
    description = Column(String(5000))

    reviews = relationship('Review', cascade='all,delete')
