def analyze_text(text):
  """Analyzes a text string and returns statistics"""

  # Calculate word count
  word_count = len(text.split())

  # Calculate character count (excluding spaces)
  char_count = len(text.replace(" ", ""))

  # Find unique words (case-insensitive)
  unique_words = set(text.lower().split())  # Convert to lowercase and use a set for uniqueness

  # Print analysis results
  print(f"Word count: {word_count}")
  print(f"Character count (excluding spaces): {char_count}")
  print(f"Unique words: {len(unique_words)}")

# Get user input for the text
text = input("Enter some text to analyze: ")

# Analyze the text and print results
analyze_text(text)
