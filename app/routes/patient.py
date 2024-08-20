from app.routes import auth_bp
from flask import request
from app.services.auth_service import register_user


@auth_bp.route('/reg_patient', methods=['POST'])
@swag_from(
    {
        "tags": ["patient Registration"],
        "description": "Register a new patient",
        "parameters": [
            {
                "name": "data",
                "description": "patient registration data",
                "in": "body",
                "required": False,
                "schema": swagger_schemas["Patient"],
            }
        ],
        "responses": {
            "201": {
                "description": "Patient registered successfully",
                "schema": {
                    "type": "object",
                    "properties": {
                        "patient": swagger_schemas["Patients"],
                    },
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    }
)
def reg_patient():
    data = request.get_json()
    return register_user(data)




