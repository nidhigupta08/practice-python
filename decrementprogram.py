# Function to increment a variable
def increment(x):
    return x + 1

# Function to decrement a variable
def decrement(x):
    return x - 1

# Example usage
num = 10

# Incrementing num by 1
num = increment(num)
print("After incrementing by 1:", num)  # Output: 11

# Decrementing num by 1
num = decrement(num)
print("After decrementing by 1:", num)  # Output: 10

# Incrementing num by 5
num += 5
print("After incrementing by 5:", num)  # Output: 15

# Decrementing num by 3
num -= 3
print("After decrementing by 3:", num)  # Output: 12
