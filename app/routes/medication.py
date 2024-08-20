from app.routes import pharmacy_bp
from flask import request
from app.services.medication import add_med, show_med


@pharmacy_bp.route("/add_medication", methods=["POST", "GET"])
def add_medication():
    data = request.get_json()
    return add_med(data)


@pharmacy_bp.route("/show_medication", methods=["GET"])
def show_medication():
    return show_med()
