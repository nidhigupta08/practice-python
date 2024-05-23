class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def display_info(self):
        print(f"Student Name: {self.get_name()}, Age: {self.get_age()}")

# Creating an instance of the Student class
student = Student("John Doe", 20)
student.display_info()

# Accessing and modifying private attributes through getter and setter methods
student.set_name("Jane Doe")
student.set_age(21)
student.display_info()

# Attempting to set an invalid age
student.set_age(-5)
