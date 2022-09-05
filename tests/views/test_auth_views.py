from unittest.mock import MagicMock

import pytest
import requests

from project.container import auth_service, user_service
from project.models import User
from project.tools.security import generate_password_hash, generate_tokens_func


class TestAuthView:

    @pytest.fixture
    def user_with_pass(self, db):
        user = User(email="email", password="Password")
        user.password = generate_password_hash("Password")
        db.session.add(user)
        db.session.commit()
        return user

    def test_register_page(self, user_with_pass):
        data = {"email": "email", "password": "password"}
        auth_service.create_user = MagicMock(return_value = user_with_pass)
        response = requests.post('/register/')

        assert response.status_code == 201

    # def test_login_page(self, client):
    #     data = {"email": "email", "password": "password"}
    #     response = client.post('/login/', data=data)
    #     auth_service.generate_tokens = MagicMock(return_value = {1: 1, 2: 2})
    #     assert response.status_code == 201
