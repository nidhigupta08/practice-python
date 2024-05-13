class Shape:
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Usage
circle = Circle(5)
print("Perimeter of circle:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Perimeter of rectangle:", rectangle.calculate_perimeter())
