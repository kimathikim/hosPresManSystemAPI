from app.models.user import OnBoarders
from app.models.doctor import Doctors
from app.models.pharmacist import Pharmacists
from app.models.patient import Patients
from app.models.admin import Admin
from app.models.user import User

import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def check_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


#
# hashed_password = hash_password("my_password")
#
# # Check a password
# if check_password("my_password", hashed_password):
#     print("Password is correct")
# else:
#     print("Password is incorrect")
#
#
# register a new Doctor ctor, Pharmacist, Patient, Admin, OnBoarder


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

    user_model = user_roles[user_role]["model"]
    user = user_model(**data)
    user.save()
    return user.to_dict()


def login_user(data):
    pass
