import numpy as np

# Create a NumPy array
array = np.arange(1, 13)
print("Original array:", array)

# Reshape the array to 3x4
reshaped_array = np.reshape(array, (3, 4))
print("Reshaped array (3x4):")
print(reshaped_array)

# Transpose the reshaped array
transposed_array = np.transpose(reshaped_array)
print("Transposed array (4x3):")
print(transposed_array)
