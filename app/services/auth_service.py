from app.models.user import OnBoarders
from app.models.doctor import Doctors
from app.models.pharmacist import Pharmacists
from app.models.patient import Patients
from app.models.admin import Admin


# register a new Doctor ctor, Pharmacist, Patient, Admin, OnBoarder


def register_user(data):
    """ "this will be used to register Doctors, Pharmacists,
    Patients, Admins, OnBoarders"""
    if data["user"] == "Doctor":
        # Add more fields as required for Doctor
        required_fields = [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
            "Hospital_id",
        ]
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}
        doctor = Doctors(**data)
        doctor.save()
        return doctor
    elif data["user"] == "Pharmacist":
        # Add more fields as required for Pharmacist
        required_fields = (
            [
                "first_name",
                "second_name",
                "phone_number",
                "email",
                "password",
                "pharmacy_id",
            ],
        )
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}
        pharmacist = Pharmacists(**data)
        pharmacist.save()
        return pharmacist
    elif data["user"] == "Patient":
        # Add more fields as required for Patient
        required_fields = [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
            "DOB",
        ]
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}
        patient = Patients(**data)
        patient.save()
        return patient
    elif data["user"] == "Admin":
        # Add more fields as required for Admin
        required_fields = [
            "first_name",
            "second_name",
            "phone_number",
            "email",
            "password",
        ]
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}
        admin = Admin(**data)
        admin.save()
        return admin
    elif data["role"] == "Hospital" or data["role"] == "Pharmacy":
        # Add more fields as required for OnBoarders
        required_fields = ["name", "city", "address"]
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}
        on_boarder = OnBoarders(**data)
        on_boarder.save()
        return on_boarder
    else:
        return {"message": "Invalid role"}


def login_user(data):
    pass
