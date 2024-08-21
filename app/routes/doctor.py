"""This module will define weverything the doctor can do"""

# 1. add the patient to the system
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.routes import hospital_bp
from app.schemas.prescription import pres
from app.services.auth_service import register_user
from flasgger import swag_from
from app.schemas.user import swagger_schemas
from app.services.prescription_service import (
    add_prescription,
    get_patient,
    add_pres_med,
)


@hospital_bp.route("/register/patient", methods=["POST"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Registration", "Hospital"],
        "description": "Register a new Patient",
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
                "description": "Registration of the patient",
                "in": "body",
                "required": False,
                "schema": swagger_schemas["Patients"],
            },
        ],
        "responses": {
            "201": {
                "description": "User registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "Admin": swagger_schemas["Patients"],
                    },
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    }
)
def register():
    data = request.get_json()
    return register_user(data)


@hospital_bp.route("/hos/<patient_code>/patient", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Hospital"],
        "description": "Get the Patient",
        "parameters": [
            {
                "name": "Authorization",
                "description": "Bearer token for authentication. Format: 'Bearer <token>'",
                "in": "header",
                "required": True,
                "type": "string",
            },
            {
                "name": "patient_code",
                "description": "The unique code of the patient",
                "in": "path",
                "required": True,
                "type": "string",
            },
        ],
        "responses": {
            "201": {
                "description": "Detailed fetched successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "Admin": swagger_schemas["Patients"],
                    },
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    }
)
def patient(patient_code):
    return get_patient(patient_code)


@hospital_bp.route("/hospital/<patient_code>/prescription", methods=["POST"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Hospital"],
        "description": "Provide a prescription for the patient",
        "parameters": [
            {
                "name": "Authorization",
                "description": "Bearer token for authentication. Format: 'Bearer <token>'",
                "in": "header",
                "required": True,
                "type": "string",
            },
            {
                "name": "patient_code",
                "description": "The unique code of the patient",
                "in": "path",
                "required": True,
                "type": "string",
            },
            {
                "name": "data",
                "description": "Write the prescription",
                "in": "body",
                "required": False,
                "schema": swagger_schemas["Patients"],
            },
        ],
        "responses": {
            "201": {
                "description": "User registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "Admin": swagger_schemas["Patients"],
                    },
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    }
)
def prescription(patient_code):
    doctors_id = get_jwt_identity()
    print(doctors_id)
    data = request.get_json()
    data["doctor_id"] = doctors_id
    print(patient_code, data)
    return add_prescription(patient_code, data)


@hospital_bp.route("/prescrition/med/<prescription_id>", methods=["POST"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Hospital"],
        "description": "Add meds for a specific prescription",
        "parameters": [
            {
                "name": "Authorization",
                "description": "Bearer token for authentication. Format: 'Bearer <token>'",
                "in": "header",
                "required": True,
                "type": "string",
            },
            {
                "name": "prescrition_id",
                "description": "The unique code of the prescription",
                "in": "path",
                "required": True,
                "type": "string",
            },
            {
                "name": "data",
                "description": "prescription Medication",
                "in": "body",
                "required": False,
                "schema": pres["Prescription"],
            },
        ],
        "responses": {
            "201": {
                "description": "Med Added successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Med": pres["Med"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def add_pres_medication(prescription_id):
    data = request.get_json()
    data["prescription_id"] = prescription_id
    return add_pres_med(data)
