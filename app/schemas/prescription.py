from marshmallow_sqlalchemy import SQLAlchemyAutoSchema as sqlalchemyautoschema
from app.models.prescription import Prescriptions


class prescriptionschema(sqlalchemyautoschema):
    class meta:
        model = Prescriptions
