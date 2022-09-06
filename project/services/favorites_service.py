from typing import Optional
from project.dao.base import BaseDAO
from project.dao.main import FavoritesDAO
from project.exceptions import ItemNotFound, UnsuitableData
from project.models import Favorites


class FavoritesService:
    def __init__(self, dao: BaseDAO, favorites_dao: FavoritesDAO) -> None:
        self.dao = dao
        self.favorites_dao = favorites_dao

    def get_all(self, user_id, page: Optional[int] = None) -> list[Favorites]:
        return self.favorites_dao.get_by_user_id(user_id)

    def add_to_favorites(self, data):
        if not self.dao.create(data):
            raise UnsuitableData(f'Incorrect data')

    def delete_from_favorites(self, data):
        if not self.favorites_dao.delete_row(**data):
            raise ItemNotFound(f"""Movie with pk={data.get("movie_id")} isn't your favorite anymore""")
