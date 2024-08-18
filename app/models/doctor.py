from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.user import Users


class Doctors(Users):
    __tablename__ = "doctors"
    is_active = Column(Boolean, nullable=False, default=False)
    on_boarder_id = Column(String(60), ForeignKey("on_boarders.id"))
    prescriptions = relationship("Prescriptions", backref="doctors")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
