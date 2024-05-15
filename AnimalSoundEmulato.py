class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Usage
dog = Dog()
print("Dog says:", dog.make_sound())

cat = Cat()
print("Cat says:", cat.make_sound())

cow = Cow()
print("Cow says:", cow.make_sound())
