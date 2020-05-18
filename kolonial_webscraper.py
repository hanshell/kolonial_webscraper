from bs4 import BeautifulSoup as Soup
import requests
import time
import re


def get_html_doc(url):
    r = requests.get(url)
    r.raise_for_status()

    return Soup(r.content, "html.parser")


def print_html_doc_body(url):
    print(get_html_doc(url).body.prettify)

def get_all_product_category_links(url):
    soup = get_html_doc(url)
    product_categories = soup.findAll("li", {"class": "parent-category"})

    product_category_links = []

    for product in product_categories:
        product_category_links.append("https://kolonial.no"+product.h4.a["href"])

    return product_category_links


# Get name, price, and weight information from product
def find_product_info(product_soup):
    name = product_soup.find("div", {"class": "name-main"})
    price = 0
    if "label-price-discounted" in str(product_soup):
        price = product_soup.find("span", {"class": "undiscounted-price"})
    else:
        price = product_soup.find("p", {"class": "price label label-price"})
    unit_price = product_soup.find("p", {"class": "unit-price"})
    return name, price, unit_price


def write_all_products_from_category_to_file(url):
    r = get_html_doc(url)
    r.raise_for_status

    category_product_soup = get_html_doc(url)
    products = category_product_soup.find_all("div", {"class": "product-list-item"})
    print(category_product_soup)


    category_file = open("scraping_results/testwrite.txt", "a")
    category_file.truncate(0)

    for product in products:
        name, price, unit_price = find_product_info(product)

        print(name.text.strip())
        print(price.text.strip())
        print(unit_price.text.strip())
        print()

        category_file.writelines([name.text.strip(), price.text.strip(), unit_price.text.strip()])
    category_file.close()


#get_all_products_from_category("https://kolonial.no/produkter/salg/")
#print_html_doc_body("https://kolonial.no/produkter/")
#print_html_doc_body("https://kolonial.no/produkter/salg/")
#category_product_soup = get_html_doc("https://kolonial.no/produkter/salg/")
#products = category_product_soup.find_all("div", {"class": "product-list-item"})

#print(products[0])

#name = products[0].find("div", {"class": "name-main"})
#price = products[0].find("p", {"class": "price label label-price"})
#unit_price = products[0].find("p", {"class": "unit-price"})