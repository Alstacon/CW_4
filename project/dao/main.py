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

    def delete_from_favorites(self, movie_id: int, user_id: int) -> None:
        movie = self._db_session.query(Favorites).filter_by(user_id=user_id, movie_id=movie_id).first()
        self._db_session.delete(movie)
        self._db_session.commit()

    def add_to_favorites(self, movie_id: int, user_id: str) -> None:
        new_user_movie = Favorites(user_id=user_id, movie_id=movie_id)
        self._db_session.add(new_user_movie)
        self._db_session.commit()

    def get_favorites(self, user_id: int) -> list[Movie]:
        return self._db_session.query(Movie).join(Favorites).filter_by(user_id=user_id).all()
