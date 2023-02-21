import os

from project.config import BASE_DIR, DevelopmentConfig, TestingConfig
from project.server import create_app


class TestConfig:
    def test_development(self):
        app_config = create_app(DevelopmentConfig).config
        assert app_config['TESTING'] is False
        assert app_config['DEBUG'] is True
        assert app_config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + BASE_DIR.joinpath('project.db').as_posix()
        assert app_config['SQLALCHEMY_ECHO'] is True

    def test_testing(self):
        app_config = create_app(TestingConfig).config
        assert app_config['TESTING'] is True
        assert app_config['DATABASE_URI'] == 'postgresql://{username}:{password}@{host}:{port}/{db_name}'.format(
            username=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST', '127.0.0.1'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            db_name=os.getenv('POSTGRES_DB')
        )
