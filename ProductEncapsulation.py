class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id    # Public attribute
        self.name = name                # Public attribute
        self.category = category        # Public attribute
        self.__price = price            # Private attribute

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price amount!")

    def display_product_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.get_price()}")

# Creating a Product object
product = Product("P101", "Laptop", "Electronics", 1200)

# Displaying product details
product.display_product_details()
# Output:
# Product ID: P101
# Name: Laptop
# Category: Electronics
# Price: $1200

# Setting new price
product.set_price(1100)
product.display_product_details()
# Output:
# Product ID: P101
# Name: Laptop
# Category: Electronics
# Price: $1100
