def print_hollow_home(height):
    # Upper triangle
    for i in range(height // 2):
        print(" " * (height // 2 - i) + "*" + " " * (2 * i - 1) + ("*" if i > 0 else ""))
    # Middle line
    print("*" * height)
    # Lower rectangle
    for i in range(height // 2):
        print("*" + " " * (height - 2) + "*")

height = int(input("Enter the height of the home: "))
print_hollow_home(height)
