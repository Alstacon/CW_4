from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

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

    users = relationship("User")


class User(models.Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, unique=True)
    surname = Column(String)
    favorite_genre = Column(Integer, ForeignKey('movie.id'))

    genres = relationship("Movie")


class UserSchema(Schema):
    id = fields.Integer(primary_key=True)
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.Integer()


class Favorites(models.Base):
    __tablename__ = 'favorites'

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, )
    movie_id = Column(Integer, ForeignKey("movie.id"), nullable=False, )

    users = relationship("User")
    movies = relationship("Movie")


class FavoritesSchema(Schema):
    id = fields.Integer(primary_key=True)
    user_id = fields.Integer()
    movie_id = fields.Integer()
