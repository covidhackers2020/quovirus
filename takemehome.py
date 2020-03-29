import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

payload = "inboundDate=2020-30-30&cabinClass=any&children=0&infants=0&country=US&currency=USD&locale=en-US&originPlace=SFO-sky&destinationPlace=LHR-sky&outboundDate=2019-03-30-01&adults=1"
headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "7cd9631a1bmsh29e6da19e03b95fp1d6c8cjsnd456db97937b",
    'content-type': "application/x-www-form-urlencoded"
    }