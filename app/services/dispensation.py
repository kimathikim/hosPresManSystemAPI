from app.models.dispensation import Dispensation
from app.models import storage
from app.models.otp import OTP
from app.services.prescription_service import update_prescription


def dispensation(data, otp_code):
    otp = storage.get_by_code(OTP, otp_code)
    if not otp:
        return {"error": "Invalid OTP code"}, 400
    update = {"is_used": True}
    storage.update(otp, update)
    if otp.is_used:
        storage.delete(obj=otp)
        return {"error": "OTP code already used"}, 400

    fields = ["prescription_id", "dispensed_by"]
    for field in fields:
        if field not in data:
            return {"error": f"field {field} not found"}, 400
    newdispensation = Dispensation(**data)
    pres = {"is_dispensed": True}
    update_prescription(pres, data["prescription_id"])
    newdispensation.save()
    print(newdispensation)
    return {"message": "successfull dispensation"}, 201


def list_medications():
    pres = storage.all(Dispensation)
    return pres
