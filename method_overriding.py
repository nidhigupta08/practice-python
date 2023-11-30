# Parent class
class Animal:
    def make_sound(self):
        print("Some generic sound")

# Child class inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Creating instances of the classes
animal = Animal()
dog = Dog()

# Calling the methods
animal.make_sound()  # Output: Some generic sound
dog.make_sound()     # Output: Woof!
