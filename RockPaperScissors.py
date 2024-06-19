import random

# Define functions for game logic
def get_user_choice():
  """Prompts the user for their choice (rock, paper, scissors)"""
  valid_choices = ["rock", "paper", "scissors"]
  while True:
    choice = input("Choose rock, paper, or scissors: ").lower()
    if choice in valid_choices:
      return choice
    else:
      print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
  """Generates a random choice (rock, paper, scissors) for the computer"""
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  """Compares user and computer choices and determines the winner"""
  # Tie conditions
  if user_choice == computer_choice:
    return "Tie"
  # Winning conditions for user
  elif user_choice == "rock" and computer_choice == "scissors":
    return "You win!"
  elif user_choice == "paper" and computer_choice == "rock":
    return "You win!"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "You win!"
  # Winning conditions for computer
  else:
    return "Computer wins!"

def play_game():
  """Runs the rock, paper, scissors game loop"""
  playing = True
  while playing:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    print(winner)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
      playing = False

  print("Thanks for playing!")

# Start the game
play_game()
