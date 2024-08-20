from app.models.dispensation import Dispensation
from flask import jsonify
from app.models import storage



def dispensation(data):
    prescription_id = data.get('prescription_id')
    pharmacy_id = data.get('pharmacy_id')
    dispensed_by = data.get('dispensed_by')

    fields = ["prescription_id", "pharmacy_id", "dispensed_by"]
    for field in fields:
        if field not in data:
            return {"error": f"field {field} not found"}
        
        newdispensation = Dispensation(
         prescription_id=prescription_id,
        pharmacy_id=pharmacy_id,
        dispensed_by=dispensed_by
    )

    newdispensation.save()
    return {"message": "successfull dispensation"}


def show_dispensation():
    medications = storage.all("Medication")
    return jsonify({"s": medications})
