def find_largest_number(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Usage
numbers = [5, 12, 7, 42, 8, 19]
largest = find_largest_number(numbers)
print(f"The largest number is: {largest}")
