from marshmallow_sqlalchemy import sqlalchemyautoschema
from app.models.doctor import Doctors


class doctorschema(sqlalchemyautoschema):
    class meta:
        model = Doctors
