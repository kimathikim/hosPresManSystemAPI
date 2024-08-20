from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.user import OnBoarders


class onBoarderschema(SQLAlchemyAutoSchema):
    class meta:
        model = OnBoarders
