def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_sum(numbers):
    return sum(numbers)

def main():
    numbers = [10, 25, 7, 42, 3, 15]

    print("Array of numbers:", numbers)
    print("Maximum number:", find_maximum(numbers))
    print("Minimum number:", find_minimum(numbers))
    print("Average of numbers:", calculate_average(numbers))
    print("Sum of numbers:", calculate_sum(numbers))

if __name__ == "__main__":
    main()
