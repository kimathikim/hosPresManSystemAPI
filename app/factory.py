from flask import Flask
from app.models import storage
from app.config import Config
from app.extensions import init_extensions
from app.routes import register_routes
from app.routes.auth import *
from app.routes.medication import *
from app.routes.dispensation import *
from app.routes.prescription import *
from app.routes.admin import *
from app.routes.doctor import *
from app.routes.pharmacy import *


storage.reload()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_extensions(app)
    register_routes(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return {"error": "Not found"}, 404

    @app.errorhandler(502)
    def internal_error(e):
        return {"error": "Internal server error"}, 502

    # Teardown
    @app.teardown_appcontext
    def teardown_db(exception):
        storage.close()

    return app
