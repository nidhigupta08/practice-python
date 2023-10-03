# n!=1 * 2 * 3 * 4.....*n
# n!=1 * 2 * 3 * 4......(n-1) * n
# n! = n * (n-1)
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial_recursive(n-1)
fact = factorial_recursive(5)
print(fact)