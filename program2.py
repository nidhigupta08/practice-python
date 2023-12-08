# Parent class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine starts.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk_horn(self):
        print(f"The {self.make} {self.model} honks its horn.")

# Creating instances of the classes
generic_vehicle = Vehicle("Generic", "Vehicle", 2023)
generic_vehicle.start_engine()

my_car = Car("Toyota", "Corolla", 2022, 4)
my_car.start_engine()
my_car.honk_horn()
