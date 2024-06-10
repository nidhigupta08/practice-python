import numpy as np

# Create two NumPy arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 25, 35, 45, 55])

# Compare elements of the arrays
comparison = array1 > array2
print("Element-wise comparison (array1 > array2):", comparison)

# Find the maximum element-wise
max_array = np.maximum(array1, array2)
print("Element-wise maximum:", max_array)
