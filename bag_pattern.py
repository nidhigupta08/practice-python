def print_carry_bag(height):
    # Print the upper part of the bag
    for i in range(height // 2):
        print(" " * (height // 2 - i) + "/" + " " * (2 * i) + "\\")

    # Print the middle part of the bag
    print("/" + "_" * (height - 2) + "\\")

    # Print the lower part of the bag
    for i in range(height // 2):
        print("|" + " " * (height - 2) + "|")

# Taking the height of the bag as input from the user
height = int(input("Enter the height of the bag: "))
print_carry_bag(height)
