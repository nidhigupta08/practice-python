# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Canine')
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Creating an instance of the Dog class
my_dog = Dog('Golden Retriever')

# Accessing attributes and methods
print(f"My dog is a {my_dog.species} of breed {my_dog.breed}.")
print(f"My dog says: {my_dog.make_sound()}")
