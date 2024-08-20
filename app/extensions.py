# from flask_limiter import Limiter
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS

ma = Marshmallow()
jwt = JWTManager()
cors = CORS()
mail = Mail()


def init_extensions(app):
    ma.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cors.init_app(app, origins="0.0.0.0")
