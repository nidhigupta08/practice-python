class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

# Usage
dog = Dog()
print("Dog sound:", dog.sound())

cat = Cat()
print("Cat sound:", cat.sound())

cow = Cow()
print("Cow sound:", cow.sound())
