from app.models.doctor import Doctors
from app.models.patient import Patients
from app.models.pharmacist import Pharmacists
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class Pharmacistschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Pharmacists
        load_only = ["password"]
        dump_only = ["email"]


class Patientschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Patients
        load_only = ["password"]
        dump_only = ["email"]


class DoctorSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Doctors
        load_only = ["password"]
        dump_only = ["email"]


spec = APISpec(
    title="Hopital Prescription Management System API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

spec.components.schema("Patients", schema=Patientschema)
spec.components.schema("Pharmacists", schema=Pharmacistschema)
spec.components.schema("Doctors", schema=DoctorSchema)
login_schemas = spec.to_dict()["components"]["schemas"]
