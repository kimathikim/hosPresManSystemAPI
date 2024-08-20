from marshmallow_sqlalchemy import SQLAlchemyAutoSchema as sqlalchemyautoschema
from app.models.prescription import Prescription


class prescriptionschema(sqlalchemyautoschema):
    class meta:
        model = Prescription
