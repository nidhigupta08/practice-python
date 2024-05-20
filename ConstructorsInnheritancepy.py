class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        return "Meow!"

# Creating instances of Dog and Cat classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

print(f"{dog.name}, {dog.breed}: {dog.make_sound()}")
print(f"{cat.name}, {cat.color}: {cat.make_sound()}")
