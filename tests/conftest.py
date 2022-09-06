from typing import Optional

import pytest

from project.config import TestingConfig
from project.models import User
from project.server import create_app
from project.setup.db import db as database
from project.tools.security import generate_password_hash, generate_tokens_func


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client


@pytest.fixture
def user_with_pass(db):
    user = User(email="email", password="Password")
    user.password = generate_password_hash("Password")
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def create_auth_user():
    _counter = 0

    def wrapper(_id: Optional[int] = None, email: str = ''):
        nonlocal _counter
        if _id is None:
            _id = _counter
        if not email:
            email = f'test_{_id}@mail.ru'
        user = User(id=_id, email=email)
        tokens = generate_tokens_func(user)
        _counter += 1
        return user, 'Bearer {access_token}'.format(**tokens)

    return wrapper


@pytest.fixture
def token(db, create_auth_user):
    _, token = create_auth_user(1, "email")
    return token
