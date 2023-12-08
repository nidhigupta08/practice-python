# Parent class
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, breed, sound):
        super().__init__("Dog", sound)
        self.breed = breed

    def wag_tail(self):
        print(f"The {self.breed} dog wags its tail.")

# Creating instances of the classes
generic_animal = Animal("Unknown", "generic")
generic_animal.make_sound()

golden_retriever = Dog("Golden Retriever", "bark")
golden_retriever.make_sound()
golden_retriever.wag_tail()
