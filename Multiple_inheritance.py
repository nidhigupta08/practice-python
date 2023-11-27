# First parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Second parent class
class Flyable:
    def __init__(self, can_fly):
        self.can_fly = can_fly

    def fly(self):
        return "Flying high!"

# Child class inheriting from both Animal and Flyable
class Bird(Animal, Flyable):
    def __init__(self, species, can_fly):
        Animal.__init__(self, species)
        Flyable.__init__(self, can_fly)

    def make_sound(self):
        return "Chirp!"

# Creating an instance of the Bird class
my_bird = Bird('Sparrow', True)

# Accessing attributes and methods
print(f"My bird is a {my_bird.species}.")
print(f"My bird says: {my_bird.make_sound()}")
print(f"My bird can fly: {my_bird.can_fly}")
print(f"My bird is {my_bird.fly()}")
