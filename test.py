from app.models.doctor import Doctors
from app.models import storage
from app.models.prescription import Prescription
from app.models import storage

pres = Prescription(
    prescription_code="123456",
    patient_id="123456",
    doctor_id="123456",
    comment="comment",
    updated_by="123456",
)
pres.save()
print(pres.to_dict())
