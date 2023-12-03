from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Concrete subclass implementing the abstract class
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Concrete subclass implementing the abstract class
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of the concrete subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the make_sound methods
print(f"{dog.name} says: {dog.make_sound()}")  # Output: Buddy says: Woof!
print(f"{cat.name} says: {cat.make_sound()}")  # Output: Whiskers says: Meow!
