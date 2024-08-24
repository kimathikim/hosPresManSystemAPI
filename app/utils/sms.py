#!/usr/bin/env python4
from dotenv import load_dotenv
import africastalking
import os

load_dotenv()

# Initialize Africa's Talking

uname = "ImmunSys"
api_key = "91a098b314aeda715976967be01d9127f00d619fedd5157385977c4185d4061e"
africastalking.initialize(
    username="ImmunSys",
    api_key=os.getenv("AFSAPI"),
)


# class SendSMS:
#     def sending(self):
#         recipients = ["+254796699970", "+254787353102"]
#         message = "Hello mavin. Welcome to immunization tracking system.\nWe value the health of your Child!"
#         sender = 796699970
#         print(sender, recipients, message)
#         try:
#             sms = africastalking.SMS
#             print(sms)
#             response = sms.send(
#                 message,
#                 recipients,
#             )
#             print(response)
#         except Exception as e:
#             print(f"Houston, we have a problem: {e}")
#
#
# sms_instance = SendSMS()
# sms_instance.sending()


def send_code_to_patient(phone_number, patient_code):
    """This function sends a patient code via SMS."""
    try:
        message = f"Hello, your patient code is {patient_code}."
        recipients = [f"+254{phone_number}"]
        africastalking.initialize(uname, api_key)
        sender = 796699970
        print(sender, recipients, message)
        try:
            sms = africastalking.SMS
            if sms is not None:
                response = sms.send(message, recipients)
                print(response)
        except Exception as e:
            print(f"Mother father, we have a problem: {e}")
    except Exception as e:
        print(f"Mother father, we have a problem: {e} ")
    finally:
        print("At least you tried!!")
