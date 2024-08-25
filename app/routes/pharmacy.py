"""Thuis moduel contains the routes for the pharmacy module."""

from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.pharmacist import Pharmacists
from app.models import storage
from app.services.dispensation import dispensation
from flask import request, jsonify
from flasgger import swag_from
from app.routes import pharmacy_bp
from app.services.prescription_service import (
    update_prescription,
    get_prescription,
    get_all_prescriptions,
)
from app.schemas.prescription import pres


@pharmacy_bp.route("/prescription/<pres_id>", methods=["PATCH"])
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
                "schema": pres["OTP"],
            },
        ],
        "responses": {
            "201": {
                "description": "Med Added successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Prescription": pres["Prescription"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def update_pres(pres_id):
    """Thisn route will allow the pharmacy to update the prescription details"""
    data = request.get_json()
    data["updated_by"] = get_jwt_identity()
    return update_prescription(data, pres_id)


@pharmacy_bp.route("/otp/<otp_code>", methods=["GET"])
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
                "schema": pres["OTP"],
            },
        ],
        "responses": {
            "201": {
                "description": "Med Added successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Prescription": pres["Prescription"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def prescription(otp_code):
    return get_prescription(otp_code)


@pharmacy_bp.route("/dis/<pres_id>", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Pharmacy"],
        "description": "Dispense medication based   on a prescription.",
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
                "description": "Dispensation data",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "prescription_id": {"type": "string"},
                    },
                    "required": ["prescription_id", "pharmacy_id", "dispensed_by"],
                },
            },
        ],
        "responses": {
            "201": {
                "description": "Medication dispensed successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"},
                    },
                },
            },
            "400": {"description": "Bad request - Missing required fields"},
            "500": {"description": "Server error"},
        },
    }
)
def dispense_medication(pres_id):
    print("pres_id", pres_id)
    data = {}
    data["prescription_id"] = pres_id
    pharmacist_id = get_jwt_identity()
    pharmacist = storage.get(Pharmacists, pharmacist_id)
    if pharmacist is None:
        return jsonify({"error": "Failed"})
    if pharmacist.pharmacy_id is None:
        return jsonify({"error": "Access Denied"}), 403
    data["dispensed_by"] = pharmacist_id
    return dispensation(data)


@pharmacy_bp.route("/prescriptions", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Hospital", "Pha"],
        "description": "Add meds for a specific prescription",
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
            "200": {
                "description": "Retrieved successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Prescription": pres["Prescription"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def get_prescriptions():
    """This route will return all the prescriptions"""
    prescriptions = get_all_prescriptions()
    return {"prescriptions": prescriptions}
