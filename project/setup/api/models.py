from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тим Бертон'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_lenght=100, example='Йеллоустоун'),
    'description': fields.String(required=True, max_lenght=100, example='Описание'),
    'trailer': fields.String(required=True, max_lenght=100, example='https://www.youtube.com/watch?v=nDzZvwtBSJk'),
    'year': fields.Integer(required=True, example=2000),
    'rating': fields.Float(required=True, example=6.7),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1),
    'genre': fields.Nested(genre),
    'director' : fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, example="email"),
    'password': fields.String(required=True, example="password"),
    'name': fields.String(required=True, example='name'),
    'surname': fields.String(required=True, example='surname'),
    'favorite_genre': fields.Nested(genre)
})

favorites: Model = api.model('Избранное',{
    'user_id': fields.Integer(required=True, example=1),
    'movie_id': fields.Integer(required=True, example=1)
})
