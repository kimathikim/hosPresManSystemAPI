from app.routes import pharmacy_bp
from flask import request, jsonify
from app.services.medication import add_med, show_med, update_med
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from
from app.models import storage
from app.models.pharmacist import Pharmacists
from app.schemas.prescription import pres


@pharmacy_bp.route("/add_medication", methods=["POST"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Pharmacy"],
        "description": "Get the prescription for the patient",
        "parameters": [
            {
                "name": "Authorization",
                "description": "Bearer token for authentication. Format: 'Bearer <token>'",
                "in": "header",
                "required": True,
                "type": "string",
            },
            {
                "name": "data",
                "description": "prescription Medication",
                "in": "body",
                "required": False,
                "schema": pres["Medication"],
            },
        ],
        "responses": {
            "201": {
                "description": "Med Added successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Prescription": pres["Medication"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def add_medication():
    data = request.get_json()
    phamacist_id = get_jwt_identity()
    try:
        phamacist = storage.get(Pharmacists, phamacist_id)
    except:
        return jsonify({"error": "Failed"})

    if phamacist is None:
        return jsonify({"error": "Failed"})
    if phamacist.pharmacy_id is None:
        return jsonify({"error": "Acess Denied"}), 403
    data["pharmacy_id"] = phamacist.pharmacy_id
    data["pharmacy_id"] = phamacist.pharmacy_id

    return add_med(data)


@pharmacy_bp.route("/show_medication", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Pharmacy"],
        "description": "Get the prescription for the patient",
        "parameters": [
            {
                "name": "Authorization",
                "description": "Bearer token for authentication. Format: 'Bearer <token>'",
                "in": "header",
                "required": True,
                "type": "string",
            },
        ],
        "responses": {
            "201": {
                "description": "Med Added successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Prescription": pres["Medication"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def show_medication():
    return show_med()


# update medication
@pharmacy_bp.route("/update_medication/{med_id}", methods=["PUT"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Pharmacy"],
        "description": "Get the prescription for the patient",
        "parameters": [
            {
                "name": "Authorization",
                "description": "Bearer token for authentication. Format: 'Bearer <token>'",
                "in": "header",
                "required": True,
                "type": "string",
            },
            {
                "name": "data",
                "description": "prescription Medication",
                "in": "body",
                "required": False,
                "schema": pres["Medication"],
            },
        ],
        "responses": {
            "201": {
                "description": "Med Added successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Prescription": pres["Medication"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def update_medication(med_id):
    data = request.get_json()
    return update_med(med_id, data)
