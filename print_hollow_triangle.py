def print_hollow_triangle(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print("*" * i)
        else:
            print("*" + " " * (i - 2) + "*")

rows = int(input("Enter the number of rows for the triangle: "))
print_hollow_triangle(rows)
