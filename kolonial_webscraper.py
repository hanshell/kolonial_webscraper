from bs4 import BeautifulSoup as Soup
import requests


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



links = get_all_product_category_links("https://kolonial.no/produkter/")

for link in links:
    print(link)


def get_all_products_from_category(url):
    prooduct_categories =

#product_categories = get_all_product_categories("https://kolonial.no/produkter/")
#print(product_categories)


#link = product_categories.find("ul", {"class": "collapse navbar-collapse"})
#link = product_categories.ul
#print(link)


#product_categories = get_all_product_categories("https://kolonial.no/produkter/", )


#print_html_doc_body("https://kolonial.no/kategorier/401-blomster-og-planter/")