from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import UserSchema
from project.tools.decorators import auth_required

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @auth_required
    def get(self, user):
        user = user_service.get_item(user.email)
        response = UserSchema().dump(user)
        return response, 200

    @auth_required
    def patch(self, user):
        data = request.json
        user_service.update(user, data)
        return "", 204


@api.route('/password/')
class UserPassChangeView(Resource):
    @auth_required
    def put(self, user):
        data = request.json
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        user_service.update_password(user, old_password, new_password)
        return "", 204
