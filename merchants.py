class warehouse:
    def __init__(self, city, country, coordinates, stock):
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock

class product:
    def __init__(self, product, warehouses):
        self.product = product
        self.warehouses = warehouses

class buyer:
    def __init__(self, name, city, country, coordinates):
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates

class order:
    def __init__(self, buyer, product, quantity):
        self.buyer = buyer
        self.product = product
        self.quantity = quantity

class data:
    def __init__(self):
        self.products = []
