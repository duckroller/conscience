from flask import Flask, request, redirect
import twilio.twiml
import requests
import json
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
    content = request.values.get('Body', None)
    media = request.values.get('NumMedia', None)
    resultText = json.loads(barkCheck(content).text)
    if int(media) != 0:
        image = request.form['MediaUrl0']
        resultImage = json.loads(clarifaiCheck(image).text)['results'][0]['result']['tag']['classes'][0]
        probability = json.loads(clarifaiCheck(image).text)['results'][0]['result']['tag']['probs'][0]
        if resultText["success"] == False:
            if resultImage == 'nsfw' and probability >= .85:
    #            makeCall = True
                message = "This is your conscience speaking, you know you shouldn't have sent that photo"
            else:
                message = "Your message doesn't make sense, but you're fine! "
        else:
            if resultText["abusive"] == False and resultImage == 'sfw':
                message = "Not abusive at all, you are good to go! "
            else:
    #            makeCall = True
                message = "Hey stop! I see what you did there! "
    elif int(media) == 0:
        if resultText["success"] == False:
            message = "Your message doesn't make sense, but you're fine! "
        else:
            if resultText["abusive"] == False:
                message = "Not abusive at all, you are good to go! "
            else:
    #            makeCall = True
                message = "Hey stop! I see what you did there! "
    else:
        message = "This is your conscience speaking!"

    resp = twilio.twiml.Response()
    resp.message(message)
    resp.say(message)
    #resp.say(message)
    #if makeCall:
    #    execfile("make_call.py " + getNumber())

    return str(resp)


# Get these credentials from http://twilio.com/user/account
if __name__ == "__main__":
    app.run(debug=True)
