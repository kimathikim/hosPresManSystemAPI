from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.patient import Patients


class patientschema(SQLAlchemyAutoSchema):
    class meta:
        model = Patients
