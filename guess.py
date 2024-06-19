import random

# Define number guessing game functions
def generate_number():
  """Generates a random number between 1 and 100 (inclusive)"""
  return random.randint(1, 100)

def get_guess():
  """Prompts the user for a guess and ensures it's a valid integer"""
  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
      if 1 <= guess <= 100:
        return guess
      else:
        print("Invalid guess. Please enter a number between 1 and 100.")
    except ValueError:
      print("Invalid guess. Please enter a number.")

def play_game():
  """Runs the number guessing game loop"""
  target_number = generate_number()
  guesses = 0
  playing = True

  while playing:
    guess = get_guess()
    guesses += 1

    if guess < target_number:
      print("Your guess is too low.")
    elif guess > target_number:
      print("Your guess is too high.")
    else:
      playing = False
      print(f"You guessed it in {guesses} tries! Congratulations!")

  # Optionally, ask if the user wants to play again

# Start the game
play_game()

print("Thanks for playing!")
