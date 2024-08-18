from marshmallow_sqlalchemy import sqlalchemy_auto_schema
from app.models.user import OnBoarders


class onBoarderschema(sqlalchemy_auto_schema):
    class meta:
        model = OnBoarders
