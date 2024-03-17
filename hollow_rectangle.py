def print_hollow_rectangle(rows, cols):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * cols)
        else:
            print("*" + " " * (cols - 2) + "*")

rows = int(input("Enter the number of rows for the rectangle: "))
cols = int(input("Enter the number of columns for the rectangle: "))
print_hollow_rectangle(rows, cols)
