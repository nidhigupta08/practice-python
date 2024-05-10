class Animal:
    def feed(self):
        pass

class Dog(Animal):
    def feed(self):
        return "Give dog food"

class Cat(Animal):
    def feed(self):
        return "Give cat food"

class Bird(Animal):
    def feed(self):
        return "Give bird seeds"

# Usage
dog = Dog()
print("Feeding the dog:", dog.feed())

cat = Cat()
print("Feeding the cat:", cat.feed())

bird = Bird()
print("Feeding the bird:", bird.feed())
