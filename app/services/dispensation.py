from app.models.dispensation import Dispensation
from flask import jsonify
from app.models import storage
from app.models.medication import Medication


def dispensation(data):
    fields = ["prescription_id", "pharmacy_id", "dispensed_by"]
    for field in fields:
        if field not in data:
            return {"error": f"field {field} not found"}

    newdispensation = Dispensation(**data)
    try:
        newdispensation.save()
        return {"message": "successfull dispensation"}
    except:
        return {"error": "Failed to dispense"}


def list_medications():
    pres = storage.all(Dispensation)
    return pres
