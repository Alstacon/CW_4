from flask_restx import Namespace, Resource

from project.container import favorites_service
from project.models import FavoritesSchema
from project.tools.decorators import auth_required

api = Namespace('favorites')


@api.route('/movies/<int:movie_id>/')
class FavoritesView(Resource):
    @auth_required
    def post(self, user, movie_id):
        data = {
            "user_id": user.id,
            "movie_id": movie_id
        }
        favorites_service.add_to_favorites(data)
        return '', 201

    @auth_required
    def delete(self, user, movie_id):
        data = {
            "user_id": user.id,
            "movie_id": movie_id
        }
        favorites_service.delete_from_favorites(data)
        return '', 204

    @api.route('/movies/')
    class FavoritesView(Resource):
        @auth_required
        def get(self, user):
            favorites = favorites_service.get_all(user.id)
            response = FavoritesSchema().dump(favorites)
            return response, 200
