def get_word(prompt):
  """
  Prompts the user for a word based on the provided prompt.
  """
  while True:
    word = input(prompt + " ")
    if word.strip():  # Check for empty input (only whitespace)
      return word.strip()
    else:
      print("Please enter a word.")

def create_madlib(template):
  """
  Creates a Mad Lib story by replacing placeholders with user-provided words.
  """
  words = {}
  for placeholder in set(re.findall(r'\{(.*?)\}', template)):
    words[placeholder] = get_word(f"Enter a {placeholder}: ")

  story = template.format(**words)  # Format string with dictionary values
  return story

def play_mad_libs():
  """
  Plays a round of Mad Libs by presenting a template and collecting user input.
  """
  template = """
  There once was a {adjective} {noun} who lived in a {adjective} {noun}.
  One day, the {noun} decided to go on a {adjective} adventure.
  They met a {adjective} {noun} along the way and together they had a {adjective} time.
  """

  story = create_madlib(template)
  print("\nYour Mad Lib story:")
  print(story)

# Run the game
play_mad_libs()