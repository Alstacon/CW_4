from typing import Optional
from unittest.mock import MagicMock

import pytest

from project.container import user_service
from project.models import User
from project.tools.security import generate_tokens_func


@pytest.fixture
def create_auth_user():
    _counter = 0
    def wrapper(_id: Optional[int] = None, email: str = ''):
        nonlocal _counter
        if _id is None:
            _id =_counter
        if not email:
            email = f'test_{_id}@mail.ru'
        user = User(id=_id, email=email)
        tokens = generate_tokens_func(user)
        _counter += 1
        return user, 'Bearer {access_token}'.format(**tokens)

    return wrapper


class TestUsersView:

    @pytest.fixture
    def user_1(self, db, create_auth_user):
        user, token = create_auth_user(1, "email")
        db.session.add(user)
        db.session.commit()
        return user

    @pytest.fixture
    def token(self, db, create_auth_user):
        _, token = create_auth_user(1, "email")
        return token

    def test_user_page(self, client, token):
        user_service.get_item = MagicMock(return_value=User(id=1, email="email"))
        response = client.get('/user/', headers={'Authorization': token})
        assert response.status_code == 200

        response = client.get('/user/')
        assert response.status_code == 401




    # def test_user_update(self, client, token):
    #     user_service.update = MagicMock(return_value=User(id=1, email="email", name="name", surname="surname"))
    #     response = client.patch('/user/', headers={'Authorization': token})
    #     assert response.json == {}







