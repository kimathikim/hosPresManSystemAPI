from app.models.user import Users


class Admin(Users):
    __tablename__ = "admin"

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)
