from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.base_model import BaseClass, Base


class Dispensation(BaseClass, Base):
    __tablename__ = "dispensations"
    prescription_id = Column(String(60), ForeignKey("prescriptions.id"))
    pharmacy_id = Column(String(60), ForeignKey("on_boarders.id"))
    dispensed_by = Column(String(60), ForeignKey("pharmacists.id"))
    dispensed_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, **kwargs):
        """Initialize the Medication model"""
        super().__init__(**kwargs)
