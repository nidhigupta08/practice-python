def print_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            print("*", end=" ")
        print()

width = 8  # Width of the rectangle
height = 5  # Height of the rectangle
print_rectangle(width, height)
