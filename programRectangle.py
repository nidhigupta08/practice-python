class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Taking input for length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Creating an instance of the Rectangle class
rectangle = Rectangle(length, width)

# Calculating area and perimeter
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

# Displaying results
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
