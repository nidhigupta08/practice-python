# Creating an array
my_array = [1, 2, 3, 4, 5]

# Displaying the array
print("Array:", my_array)

# Accessing elements of the array
print("Element at index 0:", my_array[0])
print("Element at index 2:", my_array[2])

# Modifying elements of the array
my_array[3] = 10
print("Modified array:", my_array)

# Adding elements to the end of the array
my_array.append(6)
print("Array after appending:", my_array)

# Removing elements from the array
removed_element = my_array.pop(2)
print("Array after removing element at index 2:", my_array)
print("Removed element:", removed_element)

# Finding the length of the array
print("Length of the array:", len(my_array))

# Iterating over the array
print("Elements of the array:")
for element in my_array:
    print(element)
