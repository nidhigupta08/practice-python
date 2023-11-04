def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total

# Usage
num = int(input("Enter a number: "))
digit_sum = sum_of_digits(num)
print(f"The sum of digits in {num} is: {digit_sum}")
