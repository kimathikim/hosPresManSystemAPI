from flask import request, jsonify
from app.routes import auth_bp
from app.services.auth_service import login_user, register_user
from flasgger import swag_from
from app.schemas.user import swagger_schemas
from app.schemas.user_login import login_schemas
from flask_jwt_extended import jwt_required, create_access_token
from os import getenv
from dotenv import load_dotenv

load_dotenv()


@auth_bp.route("/register", methods=["POST"])
@swag_from(
    {
        "tags": ["Registration"],
        "description": "Register a new user",
        "parameters": [
            {
                "name": "data",
                "description": "User registration data. \
                first register the Roles(Hospital, Pharmacy), pharmacist and doctor. \
                Use the models below 👇",
                "in": "body",
                "required": False,
                "schema": swagger_schemas["OnBoarders"],
            }
        ],
        "responses": {
            "201": {
                "description": "User registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "patient": swagger_schemas["Patients"],
                        "pharmacist": swagger_schemas["Pharmacists"],
                        "doctor": swagger_schemas["Doctors"],
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
    print(data)
    return register_user(data)


@auth_bp.route("/login", methods=["POST"])
@swag_from(
    {
        "tags": ["User Login"],
        "description": "Login to the system",
        "parameters": [
            {
                "name": "data",
                "description": "Login with your cridetials: email and password",
                "in": "body",
                "required": False,
                "schema": login_schemas["Doctors"],
            }
        ],
        "responses": {
            "201": {
                "description": "Logged successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "pharmacist": login_schemas["Pharmacists"],
                    },
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    }
)
def login():
    data = request.get_json()
    result = login_user(data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Login failed"}), 401
