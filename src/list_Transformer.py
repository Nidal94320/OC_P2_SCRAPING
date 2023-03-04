from .html_Extractor import html_Extractor

""" Transforms book's html data into list
    list_Transformer(soup, url) """

def extract_category(soup):
    category = soup.find_all("a", href=True)
    for balise in category:
        if balise["href"].startswith("../category/books/"):
            category = balise.string
    return category

def extract_universal_product_code(soup):
    all_td = soup.find_all("td")
    universal_product_code = all_td[0].string
    return universal_product_code

def extract_price_excluding_tax(soup):
    all_td = soup.find_all("td")
    price_excluding_tax = all_td[2].string.replace("£", "")
    return price_excluding_tax

def extract_price_including_tax(soup):
    all_td = soup.find_all("td")
    price_including_tax = all_td[3].string.replace("£", "")
    return price_including_tax

def extract_number_available(soup):
    all_td = soup.find_all("td")
    number_available = all_td[5].string
    return number_available

def extract_review_rating(soup):
    review_rating = soup.find("p", class_="star-rating")
    if review_rating["class"] == ["star-rating", "One"]:
        review_rating = "1"
    elif review_rating["class"] == ["star-rating", "Two"]:
        review_rating = "2"
    elif review_rating["class"] == ["star-rating", "Three"]:
        review_rating = "3"
    elif review_rating["class"] == ["star-rating", "Four"]:
        review_rating = "4"
    else:
        review_rating = "5"
    return review_rating

""" Some books haven't product description !"""

def extract_product_description(find_product_description):
    if find_product_description==True:
        product_description=find_product_description.string
    else:
        product_description=""
    return product_description

def list_Transformer(soup, url):

    category = extract_category(soup)

    title = soup.find("li", class_="active").string

    product_description=extract_product_description(soup.find("p", class_=False))

    universal_product_code = extract_universal_product_code(soup)

    price_excluding_tax = extract_price_excluding_tax(soup)

    price_including_tax = extract_price_including_tax(soup)

    number_available = extract_number_available(soup)

    product_page_url = url

    image_url = soup.find("img", alt=title)["src"].replace(
        "../..", "http://books.toscrape.com/"
    )

    review_rating = extract_review_rating(soup)

    book = [
        category,
        title,
        product_description,
        universal_product_code,
        number_available,
        review_rating,
        price_excluding_tax,
        price_including_tax,
        product_page_url,
        image_url,
    ]
    return book

""" Extracts and Transforms book's html data into list
    ET_book(url) """

def ET_book_data(url):
    soup = html_Extractor(url)
    book_data = list_Transformer(soup, url)
    return book_data

""" Checks, Extracts and Transforms category pages into list
    ET_category_pages(category_url)"""

def ET_category_pages(category_url):

    soup=html_Extractor(category_url)

    list_pages=[]

    list_pages.append(category_url)

    while soup.find("li", class_="next"):

        next_page = soup.find("li", class_="next").find("a")["href"]
    
        next_page_url = category_url[0:-10] + next_page
    
        list_pages.append(next_page_url)
    
        soup = html_Extractor(next_page_url)

    return list_pages

""" Extracts and Transforms books url of a category into list
    ET_books_url(list_pages)"""

def ET_books_url(list_pages):
    books_url=[]
    for page in list_pages:
        soup=html_Extractor(page)
        all_a=soup.find_all("a", title=True)
        for a in all_a:
            books_url.append(a["href"].replace("../../..", "https://books.toscrape.com/catalogue"))
    return books_url

""" Extracts and Transforms data from books url into list
    ET_books_data(books_url)"""

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

def ET_books_data(books_url):
    books_data=[]
    books_data.append(HEADER)
    for book_page in books_url:
        books_data.append(ET_book_data(book_page))
    return books_data

""" Extracts and Transforms catogories url into list 
    ET_categories_url(home_page_url)"""

def ET_categories_url(home_page_url):
    soup=html_Extractor(home_page_url)
    all_a=soup.find_all("a")
    categories_url=[]
    for a in all_a:
        if(a["href"].startswith("catalogue/category/books/")):
            categories_url.append("https://books.toscrape.com/"+a["href"])
    return categories_url
    
