def reverse_number(number):
  """
  Reverses the digits of a given integer.
  """
  reversed_number = 0
  while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
  return reversed_number

def main():
  """
  Prompts the user for a number and prints its reversed form.
  """
  number = int(input("Enter a number: "))
  reversed_number = reverse_number(number)
  print(f"The reversed number is: {reversed_number}")

if __name__ == "__main__":
  main()