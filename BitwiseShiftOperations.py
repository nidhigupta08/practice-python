# Function to demonstrate bitwise left shift and right shift
def bitwise_shift_operations(a, shift_by):
    print(f"Original number: {a}")
    print(f"Left shift by {shift_by}: {a << shift_by}")
    print(f"Right shift by {shift_by}: {a >> shift_by}")

# Input an integer and the number of positions to shift
a = int(input("Enter an integer: "))
shift_by = int(input("Enter the number of positions to shift: "))

# Perform bitwise shift operations
bitwise_shift_operations(a, shift_by)
