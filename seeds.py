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
# code from stack overflow to convert 'nan' values into None to prevent sql error
df.dropna(inplace=True)


df1 = df.where((pd.notnull(df)), None)

for i in range(len(movies.title)):
    # director = movies.director[d]
    # print(director)

    db.add_all([Movie(title=movies.title[i], director=movies.director[i])])


# insert users
# db.add_all([
#     User(username='alesmonde0', email='valid@bgf.abg', password='password123'),
#     User(username='jwilloughway1',
#          email='rmebes1@sogou.com', password='password123'),
#     User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
#     User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
#     User(username='djiri4', email='gmidgley4@weather.com', password='password123')
# ])

db.commit()


db.close()
