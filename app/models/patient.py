from sqlalchemy import Column, String, Datetime
from sqlalchemy.orm import relationship
from app.models.user import Users
from app.models.base_model import BaseClass


class Patients(Users, BaseClass):
    __tablename__ = "patients"
    patient_code = Column(String(60), nullable=False, unique=True)
    DOB = Column(Datetime, nullable=False)
    location = Column(String(60), nullable=False)
    prescriptions = relationship("Prescriptions", backref="patients")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
