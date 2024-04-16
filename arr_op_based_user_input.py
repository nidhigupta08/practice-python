def create_array():
    size = int(input("Enter the size of the array: "))
    my_array = []
    print("Enter elements of the array:")
    for _ in range(size):
        element = int(input())
        my_array.append(element)
    return my_array

def display_array(arr):
    print("Array:", arr)

def find_element(arr, target):
    if target in arr:
        print(f"{target} found in the array at index {arr.index(target)}.")
    else:
        print(f"{target} not found in the array.")

def array_sum(arr):
    total = sum(arr)
    print("Sum of array elements:", total)

def array_average(arr):
    average = sum(arr) / len(arr)
    print("Average of array elements:", average)

# Main program
my_array = create_array()
display_array(my_array)

target = int(input("Enter the element to find: "))
find_element(my_array, target)

array_sum(my_array)
array_average(my_array)
