from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from app.models.base_model import BaseClass, Base
from app.models.dispensation import Dispensation
from app.models.otp import OTP


class Med(BaseClass, Base):
    __tablename__ = "meds"
    name = Column(String(128), nullable=False)
    dosage = Column(String(128), nullable=False)
    prescription_id = Column(String(60), ForeignKey(
        "prescriptions.id"), nullable=False)

    prescription = relationship("Prescription", back_populates="meds")

    def __init__(self, **kwargs):
        """Initialize the class with relevant details."""
        super().__init__(**kwargs)


class Prescription(BaseClass, Base):
    __tablename__ = "prescriptions"
    prescription_code = Column(String(60), nullable=False, unique=True)
    patient_id = Column(String(60), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(String(60), ForeignKey("doctors.id"), nullable=False)
    comment = Column(String(200), nullable=True)
    updated_by = Column(String(60), ForeignKey(
        "pharmacists.id"), nullable=True)
    is_dispensed = Column(Boolean, default=False)

    meds = relationship("Med", back_populates="prescription")
    dispensation = relationship(
        Dispensation, backref=backref("prescription", uselist=False)
    )
    OTP = relationship(OTP, backref=backref("prescription", uselist=False))

    def __init__(self, **kwargs):
        """Initialize the class with relevant details."""
        super().__init__(**kwargs)

