def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swapping: a = {a}, b = {b}")

# Input two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Call the function to swap numbers
swap_numbers(a, b)
