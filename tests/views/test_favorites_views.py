import json
from unittest.mock import MagicMock

import pytest

from project.container import user_service
from project.models import favorites, Movie


class TestFavoritesView:
    def test_add_to_favorites(self, client, token):
        data = {"movie_id": 1, "user_id": 1}
        response = client.post('/favorites/movies/1/', data=json.dumps(data),
                               headers={'Content-Type': 'application/json',
                                        'Authorization': token})

        assert response.status_code == 201

    def test_delete_from_favorites(self, client, token):
        data = {"movie_id": 1, "user_id": 1}
        user_service.add_to_favorites(**data)
        data_2 = {"movie_id": 2, "user_id": 1}
        user_service.add_to_favorites(**data_2)
        response = client.delete('/favorites/movies/1/', data=json.dumps(data),
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': token})
        assert response.status_code == 204
        assert len(user_service.get_favorites(1)) == 1

    def test_get_favorites(self, client, token, user_with_pass):
        data = {"movie_id": 1, "user_id": 1}
        user_service.add_to_favorites(**data)
        response = client.get('/favorites/movies/',
                              headers={'Content-Type': 'application/json',
                                       'Authorization': token})
        assert response.status_code == 200
        assert len(user_service.get_favorites(1)) == 0
        # assert user_service.get_favorites(1)[0].movie_id == 1
