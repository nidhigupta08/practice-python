def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print("* " * i)

rows = int(input("Enter the number of rows for the right triangle: "))
print_right_triangle(rows)
