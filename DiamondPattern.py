def print_hemisphere(rows):
    # Upper hemisphere
    for i in range(rows):
        # Print leading spaces
        for j in range(rows - i - 1):
            print(" ", end="")

        # Print pattern
        for j in range(2 * i + 1):
            print("*", end="")

        print()

    # Lower hemisphere
    for i in range(rows - 2, -1, -1):
        # Print leading spaces
        for j in range(rows - i - 1):
            print(" ", end="")

        # Print pattern
        for j in range(2 * i + 1):
            print("*", end="")

        print()


# Example usage
rows = 5
print_hemisphere(rows)
