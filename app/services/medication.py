from app.models.medication import Medication
from flask import jsonify
from app.models import storage


def add_med(data):
    name = data.get("name")
    quantity = data.get("quantity")
    pharmacy_id = data.get("pharmacy_id")
    pharmacist_id = data.get("pharmacist_id")

    fields = ["name", "quantity", "pharmacist_id", "pharmacy_id"]
    for field in fields:
        if field not in data:
            return {"error": f"field {field} not found"}

    new_medication = Medication(
        name=name,
        quantity=int(quantity),
        pharmacy_id=pharmacy_id,
        pharmacist_id=pharmacist_id,
    )

    new_medication.save()
    return {"message": "mdication added succz"}


def show_med():
    medications = storage.all("Medication")
    return jsonify({"s": medications})
