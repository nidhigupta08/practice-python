import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Usage
circle = Circle(5)
print("Area of circle:", circle.calculate_area())
print("Perimeter of circle:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Area of rectangle:", rectangle.calculate_area())
print("Perimeter of rectangle:", rectangle.calculate_perimeter())
