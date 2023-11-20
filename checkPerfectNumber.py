def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

number = 28
if is_perfect_number(number):
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")
