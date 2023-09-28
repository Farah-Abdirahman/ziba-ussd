import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'farah'
api_key = 'fb361595bc98e1a848f9dbb615d3f0df93577fbbce733a7dcb348f21af4471a8'


africastalking.initialize(username, api_key)

sms = africastalking.SMS

class SMSClient:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send_sms(self):
        sms.send(self.message, [self.phone_number], callback=on_finish)


def on_finish(error, response):
    if error is not None:
        raise error
    print(response)
