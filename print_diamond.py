def print_diamond(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)


rows = int(input("Enter the number of rows for the diamond: "))
print_diamond(rows)

