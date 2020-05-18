from bs4 import BeautifulSoup as Soup
import requests


def get_html_doc(url):
    r = requests.get(url)
    r.raise_for_status()

    return Soup(r.content)


def print_html_doc_body(url):
    print(get_html_doc(url).body.prettify)


def get_all_product_categories(url, product_div_class_name):
    soup = get_html_doc(url)
    soup.findAll("li", {})


print_html_doc_body("https://kolonial.no/kategorier/401-blomster-og-planter/")