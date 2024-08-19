"""This module defines the Medication model"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base
from app.models.user import OnBoarders
from app.models.pharmacist import Pharmacists


class Medication(BaseClass, Base):
    """Defines the Medication model"""

    __tablename__ = "medications"

    name = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False)
    pharmacy_id = Column(String(62), ForeignKey("pharmacy.id"), nullable=False)
    pharmacist_id = Column(
        String(62),
        ForeignKey(
            "pharmacist.id\
    "
        ),
        nullable=False,
    )

    pharmacist = relationship(Pharmacists, back_populates="medications")
    pharmacy = relationship(OnBoarders, back_populates="medications")

    def __init__(self, **kwargs):
        """Initialize the Medication model"""
        super().__init__(**kwargs)
