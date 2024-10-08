from datetime import timedelta
from app.services.encryption_service import generate_unique_code
from flask.json import jsonify
from app.utils.sanitization import sanitize_object
from app.utils.sms import send_code_to_patient
from app.models import storage
from flask_jwt_extended import create_access_token
import bcrypt
from app.models.admin import Admin
from app.models.patient import Patients
from app.models.pharmacist import Pharmacists
from app.models.doctor import Doctors
from app.models.user import OnBoarders
from dotenv import load_dotenv

load_dotenv()


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-7"), bcrypt.gensalt()).decode("utf-8")


def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-7"), hashed.encode("utf-8"))


user_roles = {
    "Doctor": {
        "fields": [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
            "hospital_id",
        ],
        "model": Doctors,
    },
    "Pharmacist": {
        "fields": [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
            "pharmacy_id",
        ],
        "model": Pharmacists,
    },
    "Patient": {
        "fields": [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
            "DOB",
        ],
        "model": Patients,
    },
    "Admin": {
        "fields": [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
        ],
        "model": Admin,
    },
    "Hospital": {
        "fields": ["name", "city", "address"],
        "model": OnBoarders,
    },
    "Pharmacy": {
        "fields": ["name", "city", "address"],
        "model": OnBoarders,
    },
}


def register_user(data):
    print(data)
    if data.get("role"):
        user_role = data["role"]
    elif data.get("user"):
        user_role = data["user"]
        if user_role == "Patient":
            data["patient_code"] = str(generate_unique_code())
            send_code_to_patient(data["phone_number"], data["patient_code"])

    else:
        return {"error": "Role or user is required"}

    if data.get("password"):
        data["password"] = hash_password(data["password"])

    if user_role not in user_roles:
        return {"message": "Invalid role"}

    required_fields = user_roles[user_role]["fields"]
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}

    try:
        user_model = user_roles[user_role]["model"]
        user = user_model(**data)
        user.save()
        return jsonify({"success": user.to_dict()}), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 501


def register_staff(id, data):
    """ "this will be used to register Doctors, Pharmacists,
    Patients, Admins, OnBoarders"""

    if data.get("user"):
        user_role = data["user"]
        if user_role == "Doctor":
            data["hospital_id"] = id
    elif data.get("user"):
        user_role = data["user"]
        if user_role == "Pharmacist":
            data["pharmacy_id"] = id
    else:
        return {"error": "Role or user is required"}

    if data.get("password"):
        data["password"] = hash_password(data["password"])

    if user_role not in user_roles:
        return {"message": "Invalid role"}
    required_fields = user_roles[user_role]["fields"]
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}

    try:
        user_model = user_roles[user_role]["model"]
        user = user_model(**data)
        user.save()
        return jsonify({"success": user.to_dict()}), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 501


def login_user(data):
    if data.get("email") and data.get("password"):
        user = None
        user_roles = [Pharmacists, Doctors, Admin]
        user_role = None
        for role in user_roles:
            user = storage.get_by_email(role, data["email"])
            if user:
                user_role = role
                if user_role == Pharmacists:
                    user_role = "Pharmacist"
                if user_role == Doctors:
                    user_role = "Doctor"
                if user_role == Admin:
                    user_role = "Admin"
                break
        print(user_role)
        if user and check_password(data["password"], user.password):
            access_token = create_access_token(
                identity=user.id, expires_delta=timedelta(days=2)
            )
            return jsonify({"access_token": access_token, "role": user_role}), 201
        return jsonify({"error": "Invalid credentials"}), 402
    return jsonify({"error": "Email and password required"}), 401


def get_pharmacies():
    pharmacies = [sanitize_object(pharmacy)
                  for pharmacy in storage.all(OnBoarders)]
    pharmacies_with_role_pharmacy = [
        pharmacy
        for pharmacy in pharmacies
        if pharmacy and pharmacy["role"] == "Pharmacy"
    ]
    if pharmacies_with_role_pharmacy:
        return jsonify({"pharmacies": pharmacies_with_role_pharmacy})
    return jsonify({"error": "No pharmacies found"})


def get_hospitals():
    hos = [sanitize_object(hospital) for hospital in storage.all(OnBoarders)]
    hos_with_role_hospital = [
        hospital for hospital in hos if hospital and hospital["role"] == "Hospital"
    ]
    if hos_with_role_hospital:
        return jsonify({"hospitals": hos_with_role_hospital})
    return jsonify({"error": "No hospitals found"})


def get_doctors(id):
    docs = [sanitize_object(doctor) for doctor in storage.all(Doctors)]
    doc_hos = [
        doctor for doctor in docs if doctor is not None and doctor["hospital_id"] == id
    ]

    if doc_hos:
        return jsonify({"doctors": doc_hos})
    return jsonify({"error": "No doctors found"})


def get_pharmacists(id):
    pharms = [sanitize_object(pharmacist)
              for pharmacist in storage.all(Pharmacists)]
    doc_hos = [
        pharm for pharm in pharms if pharm is not None and pharm["pharmacy_id"] == id
    ]
    if doc_hos:
        return jsonify({"pharmacies": doc_hos})
    return jsonify({"error": "No pharmacists found"})
