# Parent class
class Vehicle:
    def drive(self):
        return "Generic vehicle driving method"

# Child class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        return "Car driving on roads"

# Child class inheriting from Vehicle
class Motorcycle(Vehicle):
    def drive(self):
        return "Motorcycle maneuvering through traffic"

# Creating instances of the classes
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# Calling the drive methods
print(vehicle.drive())    # Output: Generic vehicle driving method
print(car.drive())        # Output: Car driving on roads
print(motorcycle.drive()) # Output: Motorcycle maneuvering through traffic
