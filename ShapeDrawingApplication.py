class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

# Usage
circle = Circle()
circle.draw()

rectangle = Rectangle()
rectangle.draw()

triangle = Triangle()
triangle.draw()
