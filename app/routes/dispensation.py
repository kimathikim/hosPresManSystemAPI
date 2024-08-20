from app.routes import pharmacy_bp
from flask import request, jsonify
from app.services.dispensation import dispensation
from flasgger import swag_from

@pharmacy_bp.route("/dispens_med", methods=["POST","GET"])
@swag_from(
    {
        "tags": ["Pharmacy"],
        "description": "Dispense medication based on a prescription.",
        "parameters": [
            {
                "name": "data",
                "description": "Dispensation data",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "prescription_id": {"type": "string"},
                        "pharmacy_id": {"type": "string"},
                        "dispensed_by": {"type": "string"},
                    },
                    "required": ["prescription_id", "pharmacy_id", "dispensed_by"],
                },
            }
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
def dispense_medication():
    data = request.get_json()
    return dispensation(data)

@pharmacy_bp.route("/dispens_med", methods=["GET"])
def get_dispensation_info():
    # You can customize what the GET request should return
    return jsonify({"message": "GET method is not supported for this endpoint"}), 405
