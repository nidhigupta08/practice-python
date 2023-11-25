class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Placeholder for the sound method

class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Dog')
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, breed):
        super().__init__('Cat')
        self.breed = breed

    def make_sound(self):
        return "Meow!"

# Creating instances of the Dog and Cat classes
dog = Dog('Labrador')
cat = Cat('Siamese')

# Accessing attributes and methods of the inherited classes
print(f"I am a {dog.species} of breed {dog.breed}. I say {dog.make_sound()}")
print(f"I am a {cat.species} of breed {cat.breed}. I say {cat.make_sound()}")
