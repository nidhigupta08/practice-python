# Grandparent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Parent class inheriting from Animal
class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Canine')
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Child class inheriting from Dog
class GermanShepherd(Dog):
    def __init__(self, name):
        super().__init__('German Shepherd')
        self.name = name

    def guard(self):
        return f"{self.name} is guarding the house."

# Creating an instance of GermanShepherd class
my_gsd = GermanShepherd('Rocky')

# Accessing attributes and methods
print(f"My German Shepherd's breed is {my_gsd.species}.")
print(f"{my_gsd.name} says: {my_gsd.make_sound()}")
print(my_gsd.guard())
