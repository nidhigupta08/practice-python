class Car:
    def __init__(self, make, model, year=2020):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2021)
car1.display_info()

car2 = Car("Honda", "Civic")
car2.display_info()
