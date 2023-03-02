from src.html_Extractor import html_Extractor
from src.list_Transformer import list_Transformer
from src.csv_Loader import csv_Loader

url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"

""" creating the csv header into a list """
HEADER = [
    "category",
    "title",
    "product_description",
    "universal_product_code",
    "number_available",
    "review_rating",
    "price_excluding_tax",
    "price_including_tax",
    "product_page_url",
    "image_url",
]

""" Extrating html code """
soup = html_Extractor(url)

""" Transforming html values into list """
book = list_Transformer(soup, url)

""" Load a list into a csv file in "./data/" folder """
csv_Loader(HEADER, book)
