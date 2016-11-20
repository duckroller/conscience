import requests
import json

def clarifaiCheck(inputURL):
""" takes an URL and querys clarifai's nsfw image processing, returns the JSON

inputURL    the URL in question as a string"""

    headers = {
        'Authorization': 'Bearer MVCiDHu5zOcYsBRkvzgFzVOtG8elYA',
    }

    urlToCheck = 'https://api.clarifai.com/v1/tag/?model=nsfw-v1.0&url=' + inputURL

    return requests.get(urlToCheck, headers=headers)


r = clarifaiCheck("http://cdn.shopify.com/s/files/1/0725/3353/products/butt_lifter_1024x1024.jpg?v=1442187635")
print(r.status_code)
print(r.text)
