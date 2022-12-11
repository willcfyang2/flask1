import requests, uuid, json

"""
中英文切换
"""
key = "2624f762e0d642769e530585d40e444b"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def zh_to_en(text):
    params = {
        'api-version': '3.0',
        'from': 'zh',
        'to': ['en']
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    print(response)
    return response


def en_to_zh(text):
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['zh']
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    return response