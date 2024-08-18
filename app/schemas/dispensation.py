from marshmallow_sqlalchemy import sqlalchemyautoschema
from app.models.dispensation import Dispensation as dispensation


class dispensationschema(sqlalchemyautoschema):
    class meta:
        model = dispensation
