# Check if a number is prime
def is_prime(n):
    """Returns True if n is a prime number, False otherwise.

  Args:
    n: The number to check.

  Returns:
    True if n is a prime number, False otherwise.
  """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Get the input from the user
n = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(n):
    print("{} is a prime number.".format(n))
else:
    print("{} is not a prime number.".format(n))