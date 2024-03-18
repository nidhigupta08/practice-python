def print_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "* " * i)

rows = int(input("Enter the number of rows for the inverted pyramid: "))
print_inverted_pyramid(rows)
