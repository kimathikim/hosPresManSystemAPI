"""Thuis moduel contains the routes for the pharmacy module."""

from flask import request
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
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
