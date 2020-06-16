from products import ProductCategory
from scraper import Scraper


class KolonialScraper(Scraper):

    def __init__(self, url):
        super().__init__(url)

        self.categories = []


    # Find all product categories (Ex: Pålegg)
        product_categories = self.root_soup.findAll("li", {"class": "parent-category"})
        for product_category in product_categories:
            category_url = "https://kolonial.no"+product_category.h4.a["href"]

            split_string = category_url.split("/")
            category_name = split_string[len(split_string)-2]
#            print(category_name, category_url)

            self.categories.append(ProductCategory(category_name, category_url))

    def get_categories(self):
        return self.categories

    def print_categories(self):
        for product_category in self.categories:
            print(product_category.get_category_name() + " " + product_category.get_category_url())


kolonial_scraper = KolonialScraper("https://www.kolonial.no")
product_number=0

#kolonial_scraper.get_categories()[0].print_product_list()
#print(len(kolonial_scraper.get_categories()[0].get_product_list()))

#kolonial_scraper.print_categories()
for category in kolonial_scraper.get_categories():
    print("-------------START CATEGORY-------------")
    print(category.get_category_name())
    category.print_product_list()
    print("-------------END CATEGORY-------------")
    print()
#print("TOTAL NUMBER OF PRODUCTS: ", product_number)
#print(len(kolonial_scraper.get_categories()))
#kolonial_scraper.find_all_categories()
#kolonial_scraper.print_categories()
