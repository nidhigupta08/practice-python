def lcm(number1, number2):
    gcd = gcd(number1, number2)
    return number1 * number2 // gcd


# Example usage:
print(lcm(12, 18))
