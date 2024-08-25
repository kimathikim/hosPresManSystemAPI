from app.routes import pharmacy_bp
from flask import jsonify
from app.services.dispensation import list_medications
from flasgger import swag_from
from app.schemas.dispensation import dis


@pharmacy_bp.route("/dispens_med", methods=["GET"])
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Pharmacy"],
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
            "201": {
                "description": "Dispended successfully",
                "schema": {
                    "type": "object",
                    "properties": {"Med": dis["Dispensation"]},
                },
            },
            "400": {"description": "Bad request"},
            "500": {"description": "Server error"},
        },
    },
)
def get_dispensation_info():
    despensed = list_medications()
    return jsonify({"success": despensed}), 200
