from unittest.mock import patch

import pytest

from project.config import TestingConfig
from project.models import User
from project.server import create_app
from project.services import UsersService
from project.setup.db import db as database


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


