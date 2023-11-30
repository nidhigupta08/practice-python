# Parent class
class Shape:
    def area(self):
        return 0

# Child class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Child class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Creating instances of the classes
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Calling the area methods
print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 50
print(f"Area of the circle: {circle.area()}")        # Output: Area of the circle: 153.86 (approx.)
