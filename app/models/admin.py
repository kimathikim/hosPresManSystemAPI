from app.models.user import Users
from app.models.base_model import BaseClass


class Admin(Users, BaseClass):
    __tablename__ = "admin"

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
