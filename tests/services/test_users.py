from unittest.mock import patch, MagicMock

import pytest

from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.services import UsersService
from project.tools.security import compare_passwords, generate_password_hash


class TestUserService:

    @pytest.fixture
    @patch('project.dao.UsersDAO')
    def users_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_email.return_value = User(id=1, email="email", password="password")
        dao.get_all.return_value = [
            User(id=1, email="email", password="password"),
            User(id=2, email="liame", password="drowssap")
        ]
        dao.create.return_value = User(id=2, email="liame", password="drowssap")
        dao.update.return_value = User(id=1, email="email", password="wordpass", name="imya", surname="familia")
        return dao

    @pytest.fixture()
    def users_service(self, users_dao_mock):
        return UsersService(dao=users_dao_mock, user_dao=users_dao_mock)

    @pytest.fixture
    def user_1(self, db):
        u = User(id=1, email="email", password="password")
        db.session.add(u)
        db.session.commit()
        return u

    @pytest.fixture()
    def user_2(self, db):
        u = {"id": 2,
             "email": "liame",
             "password": "drowssap"}
        return u


    def test_get_user(self, users_service):
        user = users_service.get_item('email')
        assert user.email == 'email'

    def test_user_not_found(self, users_dao_mock, users_service):
        users_dao_mock.get_by_email.return_value = None
        with pytest.raises(ItemNotFound):
            users_service.get_item("oiuy")

    def test_create_user(self, user_2, users_service):
        user = users_service.create_user(user_2)
        assert user.email == "liame"

    def test_update(self, user_1, users_service):
        data_for_update = {
            "name": "imya",
            "surname": "familia"
        }
        user = users_service.update(user_1, data_for_update)
        assert user.name == 'imya'
        assert user.surname == 'familia'

    @pytest.mark.parametrize('passwords', ['password', 'wordpass'])
    def test_update_users_password(self, users_service, passwords, user_1, users_dao_mock):
        user_1 = users_dao_mock.update.return_value = User(id=1, email="email", password="wordpass")
        assert users_service.update_password(user_1, passwords[0], passwords[1])
        assert user_1.password == 'wordpass'




