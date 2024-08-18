from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from app.models.base_model import BaseClass, Base


class Prescription(BaseClass, Base):
    __tablename__ = "prescriptions"
    prescription_code = Column(String(128), nullable=False, unique=True)
    patient_id = Column(String(60), ForeignKey("patients.id"))
    doctor_id = Column(String(60), ForeignKey("doctors.id"))
    comment = Column(String(200), nullable=True)
    is_dispensed = Column(Boolean, default=False)
    meds = relationship("Med", backref="prescriptions")
    dispensation = relationship(
        "Dispensation", backref=backref("presctiprions", uselist=False)
    )
    OPT = relationship("OTP", backref=backref("prescriptions", uselist=False))

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)


class Med(BaseClass, Base):
    __tablename__ = "meds"
    name = Column(String(128), nullable=False)
    dosage = Column(String(128), nullable=False)
    prescription_id = Column(String(60), ForeignKey("prescriptions.id"))

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
