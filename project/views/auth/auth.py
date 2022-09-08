from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import auth_service
from project.setup.api.models import user_model
from project.setup.api.parsers import auth_parser

api = Namespace('auth')


@api.route('/login/')
class AuthView(Resource):
    def post(self):
        """Login user"""
        data = request.json

        if None in data:
            abort(400)

        tokens = auth_service.generate_tokens(data)
        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')
        if refresh_token is None:
            abort(401)
        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201


@api.route('/register/')
class AuthView(Resource):
    def post(self):
        """Create new user in db"""
        data = auth_parser.parse_args()

        auth_service.create_user(data)

        return '', 201
