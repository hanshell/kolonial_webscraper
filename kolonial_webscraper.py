from bs4 import BeautifulSoup as Soup
import requests
import datetime
import os


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

    split_string = url.split("/")
    category_name = split_string[len(split_string)-2]

    today = datetime.date.today()

    category_file = open(os.getcwd()+"/scraping_results/"+category_name+"-"+str(today)+".txt", "w+")
    category_file.truncate(0)

    for product in products:
        name, price, unit_price = find_product_info(product)

        category_file.write(name.text.strip()+"\n")
        category_file.write(price.text.strip()+"\n")
        category_file.write(unit_price.text.strip()+"\n\n")

    category_file.close()


# Write all products from all categories to files
def scrape_website(url):
    category_links = get_all_product_category_links(url)

    for link in category_links:
        write_all_products_from_category_to_file(link)


scrape_website("https://kolonial.no/produkter/")