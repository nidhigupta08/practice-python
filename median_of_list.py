def median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 0:
        # If the length of the list is even, average the two middle elements
        middle1 = sorted_numbers[length // 2 - 1]
        middle2 = sorted_numbers[length // 2]
        result = (middle1 + middle2) / 2
    else:
        # If the length is odd, return the middle element
        result = sorted_numbers[length // 2]

    return result

# Example usage:
numbers_list = [4, 2, 7, 1, 9, 3]
result = median(numbers_list)
print("Median:", result)
