from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)
hospital_bp = Blueprint("hospitals", __name__)
pharmacy_bp = Blueprint("pharmacies", __name__)


def register_routes(app):
    app.register_blueprint(hospital_bp, url_prefix="/api/v1")
    app.register_blueprint(auth_bp, url_prefix="api/v1")
    app.register_blueprint(pharmacy_bp, url_prefix="/api/v1")
