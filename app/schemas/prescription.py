from marshmallow_sqlalchemy import sqlalchemyautoschema
from app.models.prescription as Prescriptions


class prescriptionschema(sqlalchemyautoschema):
    class meta:
        model = Prescriptions
