def split_words(text):
  """
  Splits a string into a list of words, considering whitespace and punctuation.

  Args:
      text: A string to split into words.

  Returns:
      A list of words extracted from the string.
  """

  # Split the text using whitespace as delimiters by default
  words = text.split()

  # You can optionally customize the delimiter (e.g., split on commas)
  # words = text.split(',')

  return words

# Example usage
text = "This is a string with multiple words. It also has some! punctuation."
words = split_words(text)

print("Original text:", text)
print("Split words:", words)
