import requests
import json

def barkCheck(messageText):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'X-Token-Auth': 'rn4t4uzMufZYNtteRDS9hvZK',
    }

    data = "{ \"message\": \"" + messageText + "\" }"

    return requests.post('https://partner.bark.us/api/v1/messages', headers=headers, data=data)

r = barkCheck("hey asshole I hope you die")
print(r.status_code)
print(r.text)


r = barkCheck("hey sweetheart I hope to kiss")
print(r.status_code)
print(r.text)
