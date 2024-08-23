from datetime import datetime, timedelta
from app.services.encryption_service import generate_unique_code
from app.models.otp import OTP


def add_otp(prescription_id: str):
    # otp should expire after 3 daysexpires_at
    expires_at = datetime.now() + timedelta(days=3)
    otp = generate_unique_code()
    otp = OTP(otp_code=otp, prescription_id=prescription_id, expires_at=expires_at)
    try:
        otp.save()
    except Exception as e:
        return e
    return otp.to_dict()
