def find_largest_number(arr):
    if not arr:
        print("Array is empty.")
        return

    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num
    print("The largest number in the array is:", max_number)

# Main program
def main():
    # Example array
    my_array = [10, 25, 7, 42, 18, 3]

    # Find and print the largest number
    find_largest_number(my_array)

if __name__ == "__main__":
    main()
