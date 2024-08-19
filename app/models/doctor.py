from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.user import Users
from app.models.prescription import Prescription

from app.models.base_model import BaseClass, Base


class Doctors(Users, BaseClass, Base):
    __tablename__ = "doctors"
    is_active = Column(Boolean, nullable=False, default=False)
    hospital_id = Column(String(60), ForeignKey("on_boarders.id"))
    prescriptions = relationship(Prescription, backref="doctors")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
