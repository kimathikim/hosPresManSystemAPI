from sqlalchemy import Boolean, Column, ForeignKey, String
from app.models.user import Users
from sqlalchemy.orm import relationship


class Pharmacists(Users):
    __tablename__ = "pharmacists"
    is_active = Column(Boolean, nullable=False)
    on_boarder_id = Column(String(60), ForeignKey("on_boarders.id"))
    despensation = relationship("Dispensation", backref="phamacists")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
