import csv
import datetime
import urllib.request

from .list_Transformer import ET_category_pages
from .list_Transformer import ET_books_url
from .list_Transformer import ET_books_data 
from .list_Transformer import ET_categories_url

""" getting timestamp 
    datetime.datetime.now()"""

timestamp = "_" + str(datetime.datetime.now())[0:16].replace(" ", "_").replace(":", "h")

""" Load a list into a csv file 
    csv_Loader(books_data)"""

def csv_Loader(books_data,num_cat):
    output_csv = "./data/Cat" +str(num_cat)+"_"+ str(books_data[1][0]) + timestamp + ".csv"
    with open(output_csv, "w",newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        for line in books_data:
            writer.writerow(line)

""" Extracts, Transfoms and Loads all books data from one category into csv and .jpeg
    def ETL_books_data(category_url)"""

def ETL_books_data(category_url,num_cat):
    list_pages=ET_category_pages(category_url)
    books_url=ET_books_url(list_pages)
    books_data=ET_books_data(books_url)
    csv_Loader(books_data,num_cat)
    num_book=0
    for book in books_data:
        num_book+=1
        if num_book==len(books_data):
            break
        url_img_book=books_data[num_book][9]
        urllib.request.urlretrieve(url_img_book,"./data/img/"+"Cat"+str(num_cat)+"_"+"Book"+str(num_book)+".jpeg")
        

""" Extracts, Transforms and Loads all books into csv by category 
    ETL()"""
def ETL():
    home_page_url="https://books.toscrape.com/"
    num_cat=0
    for category in ET_categories_url(home_page_url):
        num_cat+=1
        ETL_books_data(category,num_cat)