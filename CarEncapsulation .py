class Car:
    def __init__(self, make, model, year, price):
        self.make = make              # Public attribute
        self.model = model            # Public attribute
        self.year = year              # Public attribute
        self.__price = price          # Private attribute

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price!")

    def display_car_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.get_price()}")

# Creating a Car object
car = Car("Toyota", "Camry", 2022, 24000)

# Displaying car details
car.display_car_details()
# Output:
# Make: Toyota
# Model: Camry
# Year: 2022
# Price: $24000

# Setting new price
car.set_price(22000)
car.display_car_details()
# Output:
# Make: Toyota
# Model: Camry
# Year: 2022
# Price: $22000
