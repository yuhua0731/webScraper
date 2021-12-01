#!/usr/bin/env python3
import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import builtwith
import whois
import json


class webScraper:
    # requests
    def test_requests_get(url):
        r = requests.get(url)
        print(r.text[:100])
    
    def test_requests_post(url, form_data):
        r = requests.post(url, data=form_data)
        print(r.text[:100])

    def test_bs4(url):
        # BeautifulSoup
        http = urllib3.PoolManager()
        r = http.request('GET', url)  # get raw data
        soup = BeautifulSoup(r.data, 'lxml')
        print(soup.title)  # display title value
        print(soup.title.text)  # convert to simple text

    def test_bs4_htmlparser(url):
        # BeautifulSoup
        r = requests.get(url)  # get raw data
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title)  # display title value
        print(soup.title.text)  # convert to simple text
        return soup

    def test_selenium(url):
        # Selenium
        s = Service(r'/Users/huayu/Downloads/chromedriver')
        browser = webdriver.Chrome(service=s)
        browser.get('http://google.com')
        browser.find_element(By.XPATH, '/html/body').click()

    def test_builtwith(url):
        built = builtwith.parse(url)
        print(json.dumps(built, sort_keys=True, indent=4))

    def test_whois(url):
        print(whois.whois(url))

if __name__ == '__main__':
    print(f'simple web scraper')
    # webScraper.test_builtwith('http://47.104.247.29:6419')
    # webScraper.test_whois('microsoft.com')
    # webScraper.test_requests_get('http://localhost:7777')
    # webScraper.test_requests_post('http://localhost:7777', {'1': '11', '2': '22'})
    url='https://docs.python.org/3.10/'
    soup = webScraper.test_bs4_htmlparser(url)
    [print(i.text) for i in soup.find_all('h3')]
    