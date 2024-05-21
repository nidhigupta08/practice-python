class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def display_cart(self):
        print("Shopping Cart:", ", ".join(self.items) if self.items else "Empty")

# Creating instances of the ShoppingCart class
cart1 = ShoppingCart()
cart1.add_item("Apples")
cart1.add_item("Bananas")
cart1.display_cart()

cart2 = ShoppingCart(["Milk", "Bread"])
cart2.display_cart()
