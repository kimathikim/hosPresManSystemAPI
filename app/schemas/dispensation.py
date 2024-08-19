from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.dispensation import Dispensation as dispensation


class dispensationschema(SQLAlchemyAutoSchema):
    class meta:
        model = dispensation
