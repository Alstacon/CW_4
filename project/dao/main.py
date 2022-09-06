from typing import Optional

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User, Favorites


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def update(self, user: User):
        self._db_session.add(user)
        self._db_session.commit()


class FavoritesDAO(BaseDAO[Favorites]):
    __model__ = Favorites

    def delete_row(self, **kwargs):
        row = self._db_session.query(Favorites).filter_by(**kwargs).all()

        for ent in row:
            self._db_session.delete(ent)
            self._db_session.commit()

    def get_all_by_user_id(self, user_id, page: Optional[int] = None):
        favorites = self._db_session.query(Favorites).filter(Favorites.user_id == user_id).all()
        return favorites

