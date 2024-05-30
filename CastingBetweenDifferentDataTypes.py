# Program 2: Casting Between Different Data Types

# Initial string
string_value = "12345"

# Convert string to list
list_value = list(string_value)
print(f"The list value is: {list_value}")

# Convert string to tuple
tuple_value = tuple(string_value)
print(f"The tuple value is: {tuple_value}")

# Convert string to set
set_value = set(string_value)
print(f"The set value is: {set_value}")

# Convert list back to string
new_string_value = ''.join(list_value)
print(f"The new string value from list is: {new_string_value}")

# Convert tuple back to string
new_string_from_tuple = ''.join(tuple_value)
print(f"The new string value from tuple is: {new_string_from_tuple}")
