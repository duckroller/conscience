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


r = json.loads(clarifaiCheck("http://cdn.shopify.com/s/files/1/0725/3353/products/butt_lifter_1024x1024.jpg?v=1442187635").text)

print(r['results'][0]['result']['tag']['probs'][1]) # prints the probability the image is nsfw likely if higher than 15, almost certain if higher than 85

