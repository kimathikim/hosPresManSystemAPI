from app.models.dispensation import Dispensation
from app.models import storage
from app.services.prescription_service import update_prescription


def dispensation(data):
    fields = ["prescription_id", "dispensed_by"]
    for field in fields:
        if field not in data:
            return {"error": f"field {field} not found"}
    newdispensation = Dispensation(**data)
    pres = {"is_dispensed": True}
    update_prescription(pres, data["prescription_id"])
    try:
        newdispensation.save()
        return {"message": "successfull dispensation"}
    except:
        return {"error": "Failed to dispense"}


def list_medications():
    pres = storage.all(Dispensation)
    return pres
