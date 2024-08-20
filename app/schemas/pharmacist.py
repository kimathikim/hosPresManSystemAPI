from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.pharmacist import Pharmacists


class pharmacistschema(SQLAlchemyAutoSchema):
    class meta:
        model = Pharmacists
