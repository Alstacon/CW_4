from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'

    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)

    genre = relationship("Genre")
    director = relationship("Director")
    users = relationship("User")


class User(models.Base):
    __tablename__ = 'user'

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, unique=True)
    surname = Column(String)
    favorite_genre = Column(Integer, ForeignKey(f'{Movie.__tablename__}.id'))

    genres = relationship("Movie")


class UserSchema(Schema):
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
    user_id = fields.Integer()
    movie_id = fields.Integer()
