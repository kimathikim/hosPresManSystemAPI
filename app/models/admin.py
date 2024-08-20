from app.models.user import Users
from app.models.base_model import BaseClass, Base


class Admin(Users, BaseClass, Base):
    __tablename__ = "admin"

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
