from flasgger import Swagger, swag_from
from flask_cors import CORS
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# from flask_redis import FlaskRedis
from flask_marshmallow import Marshmallow

ma = Marshmallow()
jwt = JWTManager()
cors = CORS()
mail = Mail()
# redis_store = FlaskRedis()
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
                "authentication": "Bearer <token>",
            },
            "termsOfService": "http://tufiked/terms",
            "version": "0.0.1",
        },
        "host": "hpms-0be27dd3c23f.herokuapp.com",  # overrides localhost:500
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
    cors.init_app(app, resources={r"/api/v1*": {"origins": "*"}})
    swagger.init_app(app)


# redis_store.init_app(app)
