from flask import Flask, request, redirect
import twilio.twiml
import requests
import json
from twilio.rest import TwilioRestClient
#import sys
#import os

app = Flask(__name__)

def barkCheck(messageText):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'X-Token-Auth': 'rn4t4uzMufZYNtteRDS9hvZK',
    }

    data = "{ \"message\": \"" + str(messageText) + "\" }"

    return requests.post('https://partner.bark.us/api/v1/messages', headers=headers, data=data)

def clarifaiCheck(inputURL):
    headers = {
       'Authorization': 'Bearer MVCiDHu5zOcYsBRkvzgFzVOtG8elYA',
   }

    urlToCheck = 'https://api.clarifai.com/v1/tag/?model=nsfw-v1.0&url=' + str(inputURL)

    return requests.get(urlToCheck, headers=headers)

#def getNumber():
#    number = request.values.get('From', None)
#    return number

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #makeCall = False
    number = request.values.get('From', None)
    content = request.values.get('Body', None)
    media = request.values.get('NumMedia', None)
    resultText = json.loads(barkCheck(content).text)
    if int(media) != 0:
        image = request.form['MediaUrl0']
        resultImage = json.loads(clarifaiCheck(image).text)['results'][0]['result']['tag']['classes'][0]
        probability = json.loads(clarifaiCheck(image).text)['results'][0]['result']['tag']['probs'][0]
        if resultText["success"] == False:
            if resultImage == 'nsfw' and probability >= .85:
                makeCall(number)
                message = "This is your Conscience speaking, you know you shouldn't have sent that photo. Think about how your actions affect others."
            else:
                message = "This is your Conscience speaking. Thanks for the pic, you are good to go <3 <3 "
        else:
            if resultText["abusive"] == False and resultImage == 'sfw' and str(resultText.results["sentiment"]["polarity"]) in ['VERY_NEGATIVE', 'NEGATIVE', 'NEUTRAL']:
                message = "This is your Conscience speaking. This image is fine, you are good to go! "
            elif resultText["abusive"] == False and resultImage == 'sfw' and str(resultText.results['sentiment']['polarity']) in ['VERY_POSITIVE', 'POSITIVE']:
                message = "Your Conscience thinks you are a nice person <3"
            else:
                makeCall(number)
                message = "This is your Conscience speaking, you know you shouldn't have sent that. Think about how your actions affect others."

    elif int(media) == 0:
        if resultText["success"] == False:
            message = "This is your Conscience speaking. Your message doesn't make sense, but, urghhh you're fine! "
        else:
            if resultText["abusive"] == False and str(resultText['results']['sentiment']['polarity']) in ['VERY_NEGATIVE', 'NEGATIVE', 'NEUTRAL']:
                message = "This is your Conscience speaking. This message is fine, you are good to go! "
            elif resultText["abusive"] == False and str(resultText['results']['sentiment']['polarity']) in ('VERY_POSITIVE', 'POSITIVE'):
                message = "Your Conscience thinks you are a nice person <3"
            else:
                makeCall(number)
                message = "This is your Conscience speaking, you know you shouldn't have sent that message. Think about how your actions affect others."


    resp = twilio.twiml.Response()
#    with resp.message(message) as m:
#        m.media(imageUrl)
    resp.message(message)
    return str(resp)

@app.route("/call", methods=['GET', 'POST'])
def call():
    resp = twilio.twiml.Response()
    for i in range(5):
        resp.say("Hey, I'm your conscience. Stop being such a terrible person!")
    return str(resp)

def makeCall(number):

    account_sid = "AC90271a88fb3800a9d79b9323595beadf"
    auth_token = "64d8aa95c86d2ec9af232a3e8e6e64b4"
    client = TwilioRestClient(account_sid, auth_token)

    #caller = request.values.get("From", None)

    call = client.calls.create(to=number,  # Change it to the caller variable if possible
                               from_="+13475806502", # Must be a valid Twilio number
                               url ="https://5a33675a.ngrok.io/call"
                               )
    print(call.sid)

# Get these credentials from http://twilio.com/user/account
if __name__ == "__main__":
    app.run(debug=True)
