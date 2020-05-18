from bs4 import BeautifulSoup as Soup
import requests
from datetime import date


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


def get_all_products_from_category(url):
    r = get_html_doc(url)
    r.raise_for_status


#print_html_doc_body("https://kolonial.no/produkter/salg/")
category_product_soup = get_html_doc("https://kolonial.no/produkter/salg/")
products = category_product_soup.find_all("div", {"class": "product-list-item"})

#print(products[0])

name = products[0].find("div", {"class": "name-main"})
price = products[0].find("p", {"class": "price label label-price"})
unit_price = products[0].find("p", {"class": "unit-price"})


print(name.text.strip())
print(price.text.strip())
print(unit_price.text.strip())
print(datetime.date.today.)

#print(products[0].p[class"price label label-price"])

#product_categories = get_all_product_categories("https://kolonial.no/produkter/")
#print(product_categories)


#link = product_categories.find("ul", {"class": "collapse navbar-collapse"})
#link = product_categories.ul
#print(link)


#product_categories = get_all_product_categories("https://kolonial.no/produkter/", )


#print_html_doc_body("https://kolonial.no/kategorier/401-blomster-og-planter/")