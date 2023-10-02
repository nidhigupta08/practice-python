def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def main():
  print("The factorial of 5 is:", factorial(4))

main()