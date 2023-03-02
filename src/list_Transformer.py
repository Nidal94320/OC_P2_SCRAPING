from bs4 import BeautifulSoup

""" Transform html data into list  """


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


def list_Transformer(soup, url):

    category = extract_category(soup)

    title = soup.find("li", class_="active").string

    product_description = soup.find("p", class_=False).string

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
