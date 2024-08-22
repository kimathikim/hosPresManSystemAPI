from datetime import timedelta
from app.services.encryption_service import generate_unique_code
from flask.json import jsonify
import os
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
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def register_user(data):
    print(data)
    """ "this will be used to register Doctors, Pharmacists,
    Patients, Admins, OnBoarders"""
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

    if data.get("role"):
        user_role = data["role"]
    elif data.get("user"):
        user_role = data["user"]
        if user_role == "Patient":
            data["patient_code"] = str(generate_unique_code())
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
        return jsonify({"success": user.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def login_user(data):
    if data.get("email") and data.get("password"):
        user = None
        user_roles = [Pharmacists, Doctors, Admin]
        user_role = None
        for role in user_roles:
            user = storage.get_by_email(role, data["email"])
            if user:
                user_role = role.__name__
                break
        if user and check_password(data["password"], user.password):
            access_token = create_access_token(
                identity=user.id, expires_delta=timedelta(days=1)
            )
            return jsonify({"access_token": access_token, "role": user_role}), 200
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"error": "Email and password required"}), 400
