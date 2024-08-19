from app.models.doctor import Doctors
from app.models import storage
from app.models.user import User

on_boarder = Doctors()
on_boarder.email = "kimim"
on_boarder.first_name = "Kim"
on_boarder.second_name = "Kardashian"
on_boarder.phone_number = "1234567890"
on_boarder.user = User.Doctor
on_boarder.password = "ijiji"
on_boarder.on_boarder_id = "56ce5c03-ca5a-43f6-b798-560c83bc47a2"

on_boarder.save()

print(on_boarder)
