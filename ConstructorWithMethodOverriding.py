class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"Electric Vehicle: {self.make} {self.model}, Battery Capacity: {self.battery_capacity} kWh")

# Creating instances of Vehicle and ElectricVehicle classes
vehicle = Vehicle("Toyota", "Corolla")
vehicle.display_info()

ev = ElectricVehicle("Tesla", "Model S", 100)
ev.display_info()
