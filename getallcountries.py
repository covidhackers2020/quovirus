import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US"

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "7cd9631a1bmsh29e6da19e03b95fp1d6c8cjsnd456db97937b"
    }

response = requests.request("GET", url, headers=headers)


print(response.text)