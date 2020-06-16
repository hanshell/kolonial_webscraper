from scraper import Scraper


class ProductCategory:
    num_of_categories = 0

    def __init__(self, category_name, category_url):
        self.category_name = category_name
        self.category_url = category_url
        self.products = []

        product_category_soup = Scraper(self.category_url).get_root_soup()
        products_list = product_category_soup.find_all("div", {"class": "product-list-item"})

        for product_soup in products_list:
            self.add_product(Product(product_soup))
#            print(Product(product_soup).get_name())

        self.num_of_categories += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Can only add instance of Product")

    def get_product_list(self):
        return self.products

    def get_category_name(self):
        return self.category_name

    def get_category_url(self):
        return self.category_url

    def get_product_list(self):
        return self.products

    def print_product_list(self):
        for product in self.products:
            print(product.get_name(), product.get_price(), product.get_unit_price())

    def get_total_number_of_categories(self):
        return self.num_of_categories


class Product:
    num_of_products = 0

    def __init__(self, product_soup):
        self.name = product_soup.find("div", {"class": "name-main"}).string.strip()
        if "label-price-discounted" in str(product_soup):
            self.price = product_soup.find("span", {"class": "undiscounted-price"}).string.strip()
        else:
            self.price = product_soup.find("p", {"class": "price label label-price"}).string.strip()
        self.unit_price = product_soup.find("p", {"class": "unit-price"}).string.strip()

        self.num_of_products += 1

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_unit_price(self):
        return self.unit_price

    def get_total_number_of_products(self):
        return self.num_of_products

