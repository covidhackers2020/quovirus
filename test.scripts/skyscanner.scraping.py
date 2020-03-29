from bs4 import BeautifulSoup
from selenium_web_scraper import SeleniumWebScraper
import requests
import re

scraper = SeleniumWebScraper()

url = 'https://www.skyscanner.net/transport/flights/zrh/bkkt/200403/200410/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=true&inboundaltsenabled=true&ref=home'


soup = BeautifulSoup(scraper.retrieve_source_code(url), features="html.parser")

"""
def has_class(tag):
    return tag.has_attr('class') 

def is_result(tag):
    return re.compile('FlightsTicket_container').search(tag)
    #.find_all(re.compile("FlightsTicket_container*")):
"""


def is_ticket(tag):
    return re.compile("FlightsTicket_container").search(tag)

def has_class(tag):
    return tag.has_attr('class') and is_ticket(str(tag))

for tag in soup.find_all(has_class):
    print(tag)
    print("\n")

print("Done")
exit()

divs = soup.find_all(is_result)

#div = soup.div

print(divs)

# print(soup)
exit()



r = requests.get(url)

soup = BeautifulSoup(r.content, features="html.parser")

print(soup)


with open('http://www.google.com') as fp:
    soup = BeautifulSoup(fp)
    print(soup)

exit()

airfare_url = 'https://www.skyscanner.net/transport/flights/zrh/bkkt/200403/200410/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=true&inboundaltsenabled=true&ref=home'


with open('https://www.skyscanner.net/transport/flights/zrh/bkkt/200403/200410/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=true&inboundaltsenabled=true&ref=home') as fp:
    soup = BeautifulSoup(fp)
    print(soup)

##soup = BeautifulSoup("<html>data</html>")

# print(soup)
