import requests
import json

def barkCheck(messageText):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'X-Token-Auth': 'rn4t4uzMufZYNtteRDS9hvZK',
    }

    data = "{ \"message\": \"" + messageText + "\" }"

    return requests.post('https://partner.bark.us/api/v1/messages', headers=headers, data=data)


r = json.loads(barkCheck("hey sweetheart I hope to kiss").text)
print(r["success"])
