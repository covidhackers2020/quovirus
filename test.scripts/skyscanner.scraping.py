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
    return re.compile("BpkText_bpk-text").search(tag)

def has_class(tag):
    return tag.has_attr('class') and is_ticket(str(tag))


# BpkText_bpk-text__2NHsO BpkText_bpk-text--lg__3vAKN
"""
for span in soup.find_all('span', {'class': re.compile("BpkText_bpk-text__2NHsO")}):
    print(span)
    print("\n")
"""

for elem in soup.find_all('div', {'class': re.compile("TicketBody_container")}):
    #print(elem)

    sp = BeautifulSoup(elem.get_text())
    for left_time_span in sp.find_all('span'): #, {'class': re.compile("BpkText_bpk-text__2NHsO")}):
        print(left_time_span)
        print("\n")

print("Done")
exit()
