from project.dao import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO, FavoritesDAO

from project.services import GenresService, DirectorsService, MoviesService, UsersService, FavoritesService
from project.services.auth_service import AuthService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
favorites_dao = FavoritesDAO(db.session)


# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao, user_dao=user_dao)
auth_service = AuthService(users_service=user_service)
favorites_service = FavoritesService(dao=favorites_dao, favorites_dao=favorites_dao)