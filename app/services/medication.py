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
    return {"message": "mdication added"}


def show_med():
    medications = storage.all("Medication")
    return jsonify({"s": medications})


def update_med(med_id, data):
    if med_id is None:
        return jsonify({"error": "Medication not found"})
    medication = storage.get(Medication, med_id)
    if not medication:
        return jsonify({"error": "Medication not found"})

    medi = storage.update(medication, data)
    if medi is not None:
        return jsonify({"message": "Medication updated"})
    return jsonify({"error": "Failed"})
