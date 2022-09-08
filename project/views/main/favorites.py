from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import favorites_model

from project.tools.decorators import auth_required

api = Namespace('favorites')


@api.route('/movies/<int:movie_id>/')
class FavoritesView(Resource):
    @auth_required
    def post(self, user, movie_id):
        user_service.add_to_favorites(movie_id, user.id)
        return '', 201

    @auth_required
    def delete(self, user, movie_id):
        user_service.delete_from_favorites(movie_id, user.id)
        return '', 204

    @api.route('/movies/')
    @api.response(code=401, description='Unauthorized')
    @api.response(code=403, description='Forbidden')
    class FavoritesView(Resource):
        @auth_required
        @api.marshal_with(favorites_model, code=200)
        def get(self, user):
            return user_service.get_favorites(user.id)

