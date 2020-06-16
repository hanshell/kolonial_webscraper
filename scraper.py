from bs4 import BeautifulSoup as Soup
import requests


class Scraper:
    def __init__(self, url):
        self.r = requests.get(url)
        self.r.raise_for_status()

        self.root_soup = Soup(self.r.content, "html.parser")

    def get_root_soup(self):
        return self.root_soup

    def print_html_doc_body(self):
        print(self.root_soup.body.prettify)
