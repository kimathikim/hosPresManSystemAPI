# TODO: write the logic to get the prescription by
from flasgger.base import jsonify
from app.models import storage
from app.models.prescription import Prescription, Med
from app.services.otp_service import add_otp
from app.services.encryption_service import prescription_code
from app.models.patient import Patients
from app.models.otp import OTP

from app.utils.sanitization import sanitize_object


def add_prescription(patient_code: str, data: dict):
    data["prescription_code"] = prescription_code()
    patient = storage.get_patient_code(Patients, patient_code)
    if not patient:
        return ({"error": "Patient not found"},)
    data["patient_id"] = patient.id
    prescription = Prescription(**data)
    try:
        prescription.save()
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify((add_otp(str(prescription.id)))), 200


def get_patient(data):
    patient = storage.get_patient_code(Patients, data)
    if not patient:
        return jsonify({"error": "Patient not found"}, 404)
    return jsonify({"success": sanitize_object((patient))}), 200


def add_pres_med(data: dict):
    pres = storage.get(Prescription, data["prescription_id"])
    print(data)
    if not pres:
        return jsonify({"error": "Prescription not found"}), 400
    med = Med(**data)
    try:
        med.save()
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"success": med.to_dict()}), 201


def update_prescription(data, pres_id):
    if pres_id is None:
        return jsonify({"error": "Prescription not found"})
    pres = storage.get(Prescription, pres_id)
    if not pres:
        return jsonify({"error": pres})
    pres = storage.update(pres, data)
    if pres is not None:
        return jsonify({"message": "Prescription updated"})
    return jsonify({"error": "Failed"})


def get_prescription(otp_code):
    otp = storage.get_by_code(OTP, otp_code)
    if not otp:
        return {"error": "Invalid OTP code"}, 400
    if otp.is_used:
        storage.delete(obj=otp)
        return {"error": "OTP code already used"}, 400

    otp = sanitize_object(otp)
    if otp is None:
        return (
            {"error": "OTP not found"},
            404,
        )
    prescription = storage.get(Prescription, otp["prescription_id"])
    if prescription is None:
        return ({"error": "Prescription not found"}), 404
    medications = prescription.meds
    prescription = sanitize_object(prescription)
    if prescription is None:
        return ({"error": "Prescription not found"}), 404
    prescription["meds"] = [sanitize_object(med) for med in medications]
    return jsonify({"success": prescription}), 200


def get_all_prescriptions():
    return storage.all(Prescription)
