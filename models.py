# This file is currently not used as we're storing data in memory
# but included for future expansion with database

class Merchant:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

class Product:
    def __init__(self, id, name, description, image, price, merchant_id, phone):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.merchant_id = merchant_id
        self.phone = phone
