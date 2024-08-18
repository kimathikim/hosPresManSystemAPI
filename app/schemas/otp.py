from marshmallow_sqlalchemy import sqlalchemyautoschema
from app.models.otp import OTP


class tpschema(sqlalchemyautoschema):
    class meta:
        model = OTP
