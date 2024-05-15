import math


class Shape:
    def calculate_volume(self):
        pass


class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class Cube(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_volume(self):
        return self.side_length ** 3


# Usage
sphere = Sphere(5)
print("Volume of sphere with radius 5:", sphere.calculate_volume())

cube = Cube(4)
print("Volume of cube with side length 4:", cube.calculate_volume())
