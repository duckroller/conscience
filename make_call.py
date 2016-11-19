# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "AC90271a88fb3800a9d79b9323595beadf"
auth_token = "64d8aa95c86d2ec9af232a3e8e6e64b4"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
call = client.calls.create(to="+17652772139",  # Any phone number
                           from_="+13475806502", # Must be a valid Twilio number
                           url="https://c03a5d1f.ngrok.io/")
print(call.sid)
