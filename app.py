
from flask import *
from callus import VOICE
import os
from sendsms import SMSClient
app = Flask(__name__)


@app.route('/ussd', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    response = ""

    # ussd logic
    if text == "":
        # main menu
            response = "CON Welcome to Ziba. We offer training for tech courses for free by volunteer and peer to peer learning:\n"
            response += "1. Access Resources\n"
            response += "2. Talk to a volunteer\n"
            response += "3. Become a volunteer\n"
            response += "4. Exit"

    # sub menu
    elif text == "1":
            response = "CON choose the field \n"
            response += "1. Frontend\n"
            response += "2. Backend\n"
            response += "3. Machine Learning\n"
            response += "4. Cloud"
    elif text == "1*1":
            link = "https://medium.com/@skillcate/transfer-learning-intuition-to-implementation-5aae868361fd"
            message =f"We have sent you the link to our resource bank on Frontend: See link attached below {link}"
            sms_client = SMSClient(phone_number, message)
            sms_client.send_sms()

            response = "END Message has been sent to your phone number about your enquiry, welcome back again."
    elif text == "1*2":
            link = "https://medium.com/@skillcate/transfer-learning-intuition-to-implementation-5aae868361fd"
            message =f"We have sent you the link to our resource bank on Backend: See link attached below {link}"
            sms_client = SMSClient(phone_number, message)
            sms_client.send_sms()

            response = "END Message has been sent to your phone number about your enquiry, welcome back again."
    elif text == "1*3":
            link = "https://medium.com/@skillcate/transfer-learning-intuition-to-implementation-5aae868361fd"
            message =f"We have sent you the link to our resource bank on Ml: See link attached below {link}"
            sms_client = SMSClient(phone_number, message)
            sms_client.send_sms()

            response = "END Message has been sent to your phone number to access the resource, welcome back again."
    elif text == "1*4":
            link = "https://medium.com/@skillcate/transfer-learning-intuition-to-implementation-5aae868361fd"
            message =f"We have sent you the link to our resource bank on Cloud with AWS: See link attached below {link}"
            sms_client = SMSClient(phone_number, message)
            sms_client.send_sms()

            response = "END Message has been sent to your phone number to access the resource, welcome back again."
    elif text == "2":
            call_to = "+254723326919"
            make_call = VOICE(call_to)
            make_call.call()

            response = "END Message has been sent to your phone number to access the resource, welcome back again."
    elif text == "3":
            try:
                link = "https://forms.gle/cb4npXyhBERVM9XC8"
                message =f"We have sent you the link to Register on the volunteer form: See link attached below {link}"
                sms_client = SMSClient(phone_number, message)
                sms_client.send_sms()

                response = "END Message has been sent to your phone number to access the resource, welcome back again."

            except Exception as e:
                # show us what went wrong
                print(f"We have a problem: {e}")
    elif text == "4":
        response = "END Thank you for using our services. Welcome back again."

    # sub sub menu

    return response

@app.route('/call', methods=['POST'])
def call_back_client():
    return '<Response> <Dial phoneNumbers="" maxDuration="5"/></Response>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))

