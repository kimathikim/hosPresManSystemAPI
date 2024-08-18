from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from app.models.base_model import BaseClass, Base


class OTP(BaseClass, Base):
    __tablename__ = "otps"
    otp_code = Column(String(6), nullable=False)
    prescription_id = Column(String(60), ForeignKey("prescriptions.id"))
    expires_at = Column(String(30), nullable=False)
    is_used = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
