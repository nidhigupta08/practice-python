class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def rental_cost(self, days):
        pass


class Car(Vehicle):
    def rental_cost(self, days):
        return 50 * days


class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity

    def rental_cost(self, days):
        return 100 * days + self.load_capacity * 10


# Usage
car = Car("Toyota", "Camry", 2020)
print("Car rental cost for 3 days:", car.rental_cost(3))

truck = Truck("Ford", "F-150", 2019, 2000)
print("Truck rental cost for 5 days:", truck.rental_cost(5))
