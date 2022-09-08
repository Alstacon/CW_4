# import json
# from unittest.mock import MagicMock
#
# from project.models import Favorites
#
#
# class TestFavoritesView:
#
#     def test_add_to_favorites(self, client, token):
#         data = {"user_id": 1, "movie_id": 1}
#         response = client.post('/favorites/movies/1/', data=json.dumps(data),
#                                headers={'Content-Type': 'application/json',
#                                         'Authorization': token})
#
#         assert response.status_code == 201
#
#     def test_delete_from_favorites(self, client, token):
#         data = {"user_id": 1, "movie_id": 1}
#         favorites_service.add_to_favorites(data)
#         data_2 = {"user_id": 2, "movie_id": 1}
#         favorites_service.add_to_favorites(data_2)
#         response = client.delete('/favorites/movies/1/', data=json.dumps(data),
#                                  headers={'Content-Type': 'application/json',
#                                           'Authorization': token})
#         assert response.status_code == 204
#
#     def test_get_favorites(self, client, token):
#         data = {"user_id": 1, "movie_id": 1}
#         favorites_service.add_to_favorites(data)
#         data_1 = {"user_id": 1, "movie_id": 2}
#         favorites_service.add_to_favorites(data_1)
#         response = client.get('/favorites/movies/',
#                               headers={'Content-Type': 'application/json',
#                                        'Authorization': token})
#         assert response.status_code == 200
#         assert len(favorites_service.get_all(1)) == 2
#         assert favorites_service.get_all(1)[0].movie_id == 1
