class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes and calling a method of the Person instance
person1.greet()
