def is_all_digits(text):
  """
  Checks if a string consists only of digits (0-9).

  Args:
      text: A string to check.

  Returns:
      True if the string contains only digits, False otherwise.
  """

  # Check if all characters in the string are digits
  return all(char.isdigit() for char in text)

# Example usage
text1 = "12345"
text2 = "Hello world!"
text3 = "10 with text"

print(f"{text1} is all digits:", is_all_digits(text1))
print(f"{text2} is all digits:", is_all_digits(text2))
print(f"{text3} is all digits:", is_all_digits(text3))
