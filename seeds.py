from numpy import genfromtxt
import pandas as pd
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import User, Post, Comment, Vote, Movie, Review
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert csv data into movies
# function from stack overflow answer

movies = pd.read_csv('netflix_titles.csv', index_col=0,
                     quotechar='"', delimiter=",")

df = movies
# code from stack overflow to convert 'nan' values into None to prevent sql error when inserting an empty entry
df.dropna(inplace=True)

df1 = df.where((pd.notnull(df)), None)

for i in range(len(movies.title)):
    db.add_all([
        Movie(type=movies.type[i], title=movies.title[i],
               director=movies.director[i], cast=movies.cast[i], country=movies.country[i], date_added=movies.date_added[i], release_year=movies.release_year[i], rating=movies.rating[i], duration=movies.duration[i], description=movies.description[i])
    ])

db.commit()


db.close()
