from requests import get
from bs4 import BeautifulSoup


def html_Extractor(url):
    """ Extracts the whole html code from a web-site """

    response = get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    
    return soup
