from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from app.models.base_model import Base, BaseClass


class AuditLog(BaseClass, Base):
    """Class for capturing audit logs in the system."""

    # The action performed (e.g., "CREATE", "UPDATE", "DELETE")
    action = Column(String(255), nullable=False)
    # The type of entity being modified (e.g., "User", "Prescription")
    entity_type = Column(String(255), nullable=False)
    # ID of the entity being modified
    entity_id = Column(String(62), nullable=False)
    # ID of the user who performed the action
    performed_by = Column(String(62), ForeignKey("users.id"), nullable=False)
    timestamp = Column(
        DateTime, default=datetime.utcnow, nullable=False
    )  # When the action was performed
    # Additional details about the action (optional)
    details = Column(Text, nullable=True)

    user = relationship("Users", backref="audit_logs")

    def __init__(self, **kwargs):
        """Initialize the audit log with relevant details."""
        super().__init__(**kwargs)
