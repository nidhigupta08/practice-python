def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Example usage
base = 2
exponent = 3
print(base, "raised to the power of", exponent, "is", power(base, exponent))
