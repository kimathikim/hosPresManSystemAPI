"""This module defines the Medication model"""

from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.base_model import BaseClass, Base


class Medication(BaseClass, Base):
    """Defines the Medication model"""

    __tablename__ = "medications"

    name = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False)
    pharmacy_id = Column(String(62), ForeignKey("on_boarders.id"), nullable=False)
    pharmacist_id = Column(
        String(62),
        ForeignKey("pharmacists.id"),
        nullable=False,
    )

    def __init__(self, **kwargs):
        """Initialize the Medication model"""
        super().__init__(**kwargs)
