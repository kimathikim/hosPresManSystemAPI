# from flask_limiter import Limiter
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from flasgger import Swagger, swag_from

ma = Marshmallow()
jwt = JWTManager()
cors = CORS()
mail = Mail()
swagger = Swagger(
    template={
        "swagger": "2.0",
        "info": {
            "title": "HOSPITAL PRESCRIPTION MANAGEMENT SYSTEM API",
            "description": "API for my data",
            "contact": {
                "responsibleOrganization": "Vandi.tech",
                "responsibleDeveloper": "Brian Kimathi",
                "email": "briankimathi94@gmail.com",
                "url": "https://tufiked.live",
            },
            "termsOfService": "http://tufiked/terms",
            "version": "0.0.1",
        },
        "host": "localhost:5000",  # overrides localhost:500
        "basePath": "/api/v1",  # base bash for blueprint registration
        "schemes": ["http", "https"],
        "operationId": "getmyData",
    }
)
swag_from = swag_from


def init_extensions(app):
    ma.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cors.init_app(app, origins="0.0.0.0")
    swagger.init_app(app)
