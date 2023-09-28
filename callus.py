import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'farah'
api_key = 'fb361595bc98e1a848f9dbb615d3f0df93577fbbce733a7dcb348f21af4471a8'
at_number = os.environ.get('+254723326919')

africastalking.initialize(username, api_key)

voice = africastalking.Voice

class VOICE:
    def __init__(self, call_to):
        self.call_to = call_to

    def call(self):

        try:
			# Make the call
            result =voice.call(callFrom = at_number, callTo = [self.call_to])
            print (result)
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))
