""" P2, part2 : etracts all books from one category """
from requests import get
from bs4 import BeautifulSoup

from src.html_Extractor import html_Extractor
from src.list_Transformer import ET_books_data 
from src.list_Transformer import ET_category_pages
from src.list_Transformer import ET_books_url
from src.csv_Loader import csv_Loader

""" Intializing csv header """


""" Extracts html code from a category page
    html_Extractor(category_url)"""

category_url = ("https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
soup = html_Extractor(category_url)

""" Checks, Extracts and Transforms category pages into list
    ET_category_pages(category_url)"""

list_pages=ET_category_pages(category_url)

""" Extracts and Transforms books url of a category into list
    ET_books_url(list_pages)"""

books_url=ET_books_url(list_pages)

""" Extracts and Transforms data from books url into list
    ET_books_data(books_url)"""

books_data=ET_books_data(books_url)

""" Load a list into a csv file in data folder"""

csv_Loader(books_data)