def calculate_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start > end:
        print("Invalid input: Start value should be less than or equal to the end value.")
    else:
        result = calculate_sum(start, end)
        print(f"The sum of numbers from {start} to {end} is {result}")
except ValueError:
    print("Invalid input: Please enter valid integers for the start and end values.")

#
# Enter the start of the range: 4
# Enter the end of the range: 8
# The sum of numbers from 4 to 8 is 30