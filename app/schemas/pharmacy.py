from marshmallow_sqlalchemy import sqlalchemyautoschema
from app.models.pharmacist import Pharmacists


class pharmacistschema(sqlalchemyautoschema):
    class meta:
        model = Pharmacists
