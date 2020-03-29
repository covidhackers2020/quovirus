from selenium import webdriver
import requests


class SeleniumWebScraper():

    def __init__(self):
        self.source_code = ''
        self.is_page_loaded = 0
        self.driver = webdriver.Firefox()
        self.is_browser_closed = 0
        # To ensure the page has fully loaded we will 'implicitly' wait
        self.driver.implicitly_wait(10)  # Seconds

    def close(self):
        self.driver.close()
        self.clear_source_code()
        self.is_page_loaded = 0
        self.is_browser_closed = 1

    def clear_source_code(self):
        self.source_code = ''
        self.is_page_loaded = 0

    def retrieve_source_code(self, domain):
        if self.is_browser_closed:
            self.driver = webdriver.Firefox()
        # The driver.get method will navigate to a page given by the URL.
        #  WebDriver will wait until the page has fully loaded (that is, the "onload" event has fired)
        #  before returning control to your test or script.
        # It's worth nothing that if your page uses a lot of AJAX on load then
        #  WebDriver may not know when it has completely loaded.
        self.driver.get(domain)

        self.is_page_loaded = 1
        self.source_code = self.driver.page_source
        return self.source_code
