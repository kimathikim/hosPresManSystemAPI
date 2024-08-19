from sqlalchemy import Boolean, Column, ForeignKey, String
from app.models.user import Users
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base
from app.models.dispensation import Dispensation


class Pharmacists(Users, BaseClass, Base):
    __tablename__ = "pharmacists"
    is_active = Column(Boolean, nullable=False)
    pharmacy_id = Column(String(60), ForeignKey("on_boarders.id"))
    despensation = relationship(Dispensation, backref="pharmacists")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
