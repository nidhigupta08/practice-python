# Grandparent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Engine started."

# Parent class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"Driving the {self.brand} {self.model}."

# Child class inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, range_per_charge):
        super().__init__(brand, model)
        self.range_per_charge = range_per_charge

    def charge(self):
        return f"{self.brand} {self.model} is charging."

# Creating an instance of ElectricCar class
my_electric_car = ElectricCar('Tesla', 'Model S', '320 miles')

# Accessing attributes and methods
print(f"My electric car is a {my_electric_car.brand} {my_electric_car.model}.")
print(my_electric_car.start_engine())
print(my_electric_car.drive())
print(f"It has a range of {my_electric_car.range_per_charge}.")
print(my_electric_car.charge())
