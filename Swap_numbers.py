def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")

# Example usage
num1 = 5
num2 = 10
swap_numbers(num1, num2)
