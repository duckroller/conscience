from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

app = Flask(__name__)

def barkCheck(messageText):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'X-Token-Auth': 'rn4t4uzMufZYNtteRDS9hvZK',
    }

    data = "{ \"message\": \"" + messageText + "\" }"

    return requests.post('https://partner.bark.us/api/v1/messages', headers=headers, data=data)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    content = request.values.get('Body', None)
    result = json.loads(barkCheck(content).text)
    if result["success"] == False:
        message = "Dude! That's not even a valid message"
    else:
        if result["abusive"] == False:
            message = "Not abusive at all, you are good to go!"
        else:
            message = "Hey stop! I see what you did there!"

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
