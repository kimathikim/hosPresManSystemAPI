from flask import request, current_app
from app.routes import auth_bp
from app.services.auth_service import register_user
from flasgger import swag_from
from app.schemas.user import swagger_schemas
from flask_jwt_extended import jwt_required


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
            "201": {
                "description": "User registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "patient": swagger_schemas["OnBoarders"],
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
def register_by_admin():
    data = request.get_json()
    print(data)
    return register_user(data)
