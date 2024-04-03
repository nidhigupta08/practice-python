def print_square_pattern(size):
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()

size = 6  # Change the size as per your requirement
print_square_pattern(size)
