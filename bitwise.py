# Function to demonstrate bitwise AND, OR, and XOR
def bitwise_operations(a, b):
    print(f"Bitwise AND of {a} and {b}: {a & b}")
    print(f"Bitwise OR of {a} and {b}: {a | b}")
    print(f"Bitwise XOR of {a} and {b}: {a ^ b}")

# Input two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Perform bitwise operations
bitwise_operations(a, b)
