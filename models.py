# Models for the Arabic RTL marketplace
# Currently using simplified in-memory storage

class Merchant:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
        
    def get_id(self):
        return self.id

class Product:
    def __init__(self, id, name, description, image, price, merchant_id, phone=None):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.merchant_id = merchant_id
        self.phone = phone  # Phone number for WhatsApp contact
