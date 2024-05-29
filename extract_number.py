# Example string with a number at the end
line = "The value at the end of this line is 123.456"

# Find the position of the last space
last_space_pos = line.rfind(' ')

# Slice the string to get the number at the end
number_str = line[last_space_pos + 1:]

# Convert the extracted string to a float
number = float(number_str)

# Print the floating point number
print(number)
