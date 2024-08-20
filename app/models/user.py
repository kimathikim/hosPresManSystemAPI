from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base
from enum import Enum as UserEnum
from app.models.dispensation import Dispensation


class Role(UserEnum):
    Hospital = "Hospital"
    Pharmacy = "Pharmacy"


class User(UserEnum):
    Doctor = "Doctor"
    Pharmacist = "Pharmacist"
    Patient = "Patient"
    Admin = "Admin"


class OnBoarders(BaseClass, Base):
    __tablename__ = "on_boarders"
    name = Column(String(70), nullable=False)
    city = Column(String(70), nullable=False)
    address = Column(String(128), nullable=False, unique=True)
    role = Column(Enum(Role), nullable=False)

    doctors = relationship("Doctors", backref="on_boarders")
    pharcists = relationship("Pharmacists", backref="on_boarders")
    dispensation = relationship(Dispensation, backref="on_boarders")
    medications = relationship("Medication", backref="on_boarders")

    def __init__(self, **kwargs):
        """Initialize the class with relevant details."""
        super().__init__(**kwargs)


class Users:
    first_name = Column(String(128), nullable=False)
    second_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone_number = Column(String(128), nullable=False, unique=True)
    user = Column(Enum(User), nullable=False)
    password = Column(String(128), nullable=False)
