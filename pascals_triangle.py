def print_pascals_triangle(rows):
    for i in range(rows):
        coef = 1
        for j in range(1, rows - i):
            print(" ", end="")
        for k in range(0, i + 1):
            print(coef, end=" ")
            coef = coef * (i - k) // (k + 1)
        print()

rows = int(input("Enter the number of rows for Pascal's triangle: "))
print_pascals_triangle(rows)
