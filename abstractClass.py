from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclass implementing the abstract class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Concrete subclass implementing the abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Creating instances of the concrete subclasses
square = Square(5)
circle = Circle(7)

# Calling the area methods
print(f"Area of the square: {square.area()}")  # Output: Area of the square: 25
print(f"Area of the circle: {circle.area()}")  # Output: Area of the circle: 153.86 (approx.)
