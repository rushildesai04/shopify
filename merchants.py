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

    def output_within_country(self):
        warehouses = self.product.warehouses

        for wh in warehouses:
            if self.buyer.country != wh.country:
                warehouses.pop(wh)
        
        return warehouses
    
    def output_euc_dist(self):
        warehouses = self.product.warehouses
        min_dist = 0
        min_wh = None
        for wh in warehouses:
            euc_dist = (((self.buyer.coordinates[0] - wh.coordinates[0]) ** 2) + ((self.buyer.coordinates[1] - wh.coordinates[1]) ** 2)) ** 0.5
            if euc_dist < min_dist:
                min_dist = euc_dist
                min_wh = wh
        return min_wh

    def output_availability(self):
        warehouses = self.product.warehouses
        for wh in warehouses:
            if self.quantity > wh.stock:
                warehouses.pop(wh)
        return warehouses

class data:
    def __init__(self):
        self.products = []
