from app.services.auth_service import (
    get_pharmacies,
    get_hospitals,
    get_doctors,
    get_pharmacists,
    register_staff,
)
from flask import request, current_app
from app.routes import auth_bp
from app.services.auth_service import register_user
from flasgger import swag_from
from app.schemas.user import swagger_schemas
from flask_jwt_extended import jwt_required, get_jwt_identity


@auth_bp.route("/register", methods=["POST"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Admin"],
        "description": "Registration of system users by the admin",
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
                "description": "User registration data. \
                first register the Roles(Hospital, Pharmacy), pharmacist and doctor. \
                Use the models below 👇",
                "in": "body",
                "required": False,
                "schema": swagger_schemas["OnBoarders"],
            },
        ],
        "responses": {
            "204": {
                "description": "User registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "pharmacist": swagger_schemas["Pharmacists"],
                        "doctor": swagger_schemas["Doctors"],
                    },
                },
            },
            "403": {"description": "Bad request"},
            "503": {"description": "Server error"},
        },
    }
)
def register_by_admin():
    data = request.get_json()
    return register_user(data)


@auth_bp.route("/register/staff/<id>", methods=["POST"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Admin"],
        "description": "Registration of system users by the admin",
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
                "description": "User registration data. \
                first register the Roles(Hospital, Pharmacy), pharmacist and doctor. \
                Use the models below 👇",
                "in": "body",
                "required": False,
                "schema": swagger_schemas["OnBoarders"],
            },
        ],
        "responses": {
            "204": {
                "description": "User registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "pharmacist": swagger_schemas["Pharmacists"],
                        "doctor": swagger_schemas["Doctors"],
                    },
                },
            },
            "403": {"description": "Bad request"},
            "503": {"description": "Server error"},
        },
    }
)
def register_place_sfaff(id):
    data = request.get_json()
    return register_staff(id, data)


@auth_bp.route("/pharmacies", methods=["get"])
@jwt_required()
@swag_from(
    {
        "security": [{"bearer": []}],
        "tags": ["Admin"],
        "description": "get all hospitals",
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
                "description": "successful operation",
                "schema": {
                    "type": "array",
                    "items": swagger_schemas["OnBoarders"],
                },
            },
            "403": {"description": "forbidden"},
            "503": {"description": "server error"},
        },
    }
)
def get_all_phamacies():
    return get_pharmacies()


@auth_bp.route("/hospitals", methods=["get"])
@jwt_required()
@swag_from(
    {
        "security": [{"bearer": []}],
        "tags": ["Admin"],
        "description": "get all hospitals",
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
                "description": "successful operation",
                "schema": {
                    "type": "array",
                    "items": swagger_schemas["OnBoarders"],
                },
            },
            "403": {"description": "forbidden"},
            "503": {"description": "server error"},
        },
    }
)
def get_all_hospitals():
    return get_hospitals()


@auth_bp.route("/doctors/<hospital_id>", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Admin"],
        "description": "Get all registered doctors",
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
                "description": "Successful operation",
                "schema": {
                    "type": "array",
                    "items": swagger_schemas["Doctors"],
                },
            },
            "403": {"description": "Forbidden"},
            "503": {"description": "Server error"},
        },
    }
)
def get_all_doctors(hospital_id):
    return get_doctors(hospital_id)


@auth_bp.route("/pharmacists/<pharm_id>", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Admin"],
        "description": "Get all registered pharmacist",
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
                "description": "Successful operation",
                "schema": {
                    "type": "array",
                    "items": swagger_schemas["Pharmacists"],
                },
            },
            "403": {"description": "Forbidden"},
            "503": {"description": "Server error"},
        },
    }
)
def get_all_phamacists(pharm_id >):
    return get_pharmacists(pharm_id)
