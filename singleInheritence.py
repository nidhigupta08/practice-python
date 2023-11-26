# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"This vehicle is a {self.brand} {self.model}."

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info} It runs on {self.fuel_type}."

# Creating an instance of the Car class
my_car = Car('Toyota', 'Corolla', 'gasoline')

# Accessing attributes and methods
print(my_car.display_info())
