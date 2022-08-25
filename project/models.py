from sqlalchemy import Column, String, Integer, ForeignKey, Float

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'director'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, nullable=False)
    director_id = Column(Integer, nullable=False)


class User(models.Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, unique=True)
    surname = Column(String)
    favorite_genre = Column(String)
