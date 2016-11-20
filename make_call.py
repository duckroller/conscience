from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "AC90271a88fb3800a9d79b9323595beadf"
auth_token = "64d8aa95c86d2ec9af232a3e8e6e64b4"
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(to="+13176941608",  # Any phone number
                           from_="+13475806502", # Must be a valid Twilio number
                           ApplicationSid="AP9fe10acd6ce64163facc3f7a81ccbef3",
                           url ="https://8e9605d6.ngrok.io"
                           )
print(call.sid)
