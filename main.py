class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.total_categories += 1
        Category.total_unique_products += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def products(self):
        return "\n".join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректная")
        else:
            self.__price = value
