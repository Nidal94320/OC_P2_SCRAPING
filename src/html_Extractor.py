from requests import get
from bs4 import BeautifulSoup

""" Extract the whole html code from a web-site """


def html_Extractor(url):
    response = get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    return soup
