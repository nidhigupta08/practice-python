def boolean_operations(a, b):
    print(f"a = {a}, b = {b}")
    print(f"a AND b: {a and b}")
    print(f"a OR b: {a or b}")
    print(f"NOT a: {not a}")
    print(f"NOT b: {not b}")

# Test the function with different Boolean values
boolean_operations(True, False)
boolean_operations(False, True)
boolean_operations(True, True)
boolean_operations(False, False)
