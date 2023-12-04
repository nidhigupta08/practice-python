# Casting string to int and performing arithmetic operations
num_str = "20"
num_int = int(num_str)

# Performing addition with the casted integer
result_addition = num_int + 5

# Casting int to string for displaying the result
result_str = str(result_addition)

print(f"Original number (string): {num_str}")
print(f"Number after casting to int: {num_int}")
print(f"Result after adding 5: {result_str}")  # Output: Result after adding 5: 25
