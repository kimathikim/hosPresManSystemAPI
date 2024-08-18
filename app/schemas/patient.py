from marshmallow_sqlalchemy import sqlalchemyautoschema
from app.models.patient import Patients


class patientschema(sqlalchemyautoschema):
    class meta:
        model = Patients
