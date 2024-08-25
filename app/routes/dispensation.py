from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.sql.selectable import Alias
from werkzeug.utils import import_string
from app.routes import pharmacy_bp
from flask import request, jsonify
from app.services.dispensation import dispensation, list_medications
from flasgger import swag_from
from app.models import storage
from app.models.pharmacist import Pharmacists
from app.schemas.dispensation import dis


@pharmacy_bp.route("/dispense/{pres_id}", methods=["GET"])
@jwt_required()
@swag_from(
    {
        "security": [{"Bearer": []}],
        "tags": ["Pharmacy"],
        "description": "Dispense medication based on a prescription.",
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
