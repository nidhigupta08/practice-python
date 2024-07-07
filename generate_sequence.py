import random

def generate_sequence(length):
  """
  Generates a random sequence of numbers of specified length.
  """
  sequence = []
  for _ in range(length):
    sequence.append(random.randint(1, 10))
  return sequence

def display_sequence(sequence):
  """
  Displays the sequence of numbers for a short time.
  """
  print("Remember the sequence:")
  for number in sequence:
    print(number, end=" ")
    time.sleep(1)  # Pause for 1 second
  print()

def get_user_input(length):
  """
  Prompts the user to enter the sequence they remembered.
  """
  user_sequence = []
  for i in range(length):
    number = int(input(f"Enter number {i+1}: "))
    user_sequence.append(number)
  return user_sequence

def check_sequence(sequence, user_sequence):
  """
  Compares the user-entered sequence with the original sequence.
  """
  for i in range(len(sequence)):
    if sequence[i] != user_sequence[i]:
      return False
  return True

def play_memory_game():
  """
  Plays a round of the memory game.
  """
  sequence_length = 3  # Adjust for desired starting difficulty
  while True:
    sequence = generate_sequence(sequence_length)
    display_sequence(sequence)
    user_sequence = get_user_input(sequence_length)

    if check_sequence(sequence, user_sequence):
      print("Correct! You remembered the sequence.")
      sequence_length += 1  # Increase difficulty for the next round
    else:
      print("Incorrect. Try again.")
      break

# Import the time module for the sleep function
import time

# Run the game
play_memory_game()