from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.user import Users
from app.models.base_model import BaseClass, Base
from app.models.prescription import Prescription


class Patients(Users, BaseClass, Base):
    __tablename__ = "patients"
    patient_code = Column(String(60), nullable=False, unique=True)
    DOB = Column(String(50), nullable=False)
    location = Column(String(60), nullable=False)
    prescriptions = relationship(Prescription, backref="patients")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
