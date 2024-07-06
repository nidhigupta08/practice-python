import random

def play_rock_paper_scissors():
  """
  Plays a game of Rock, Paper, Scissors against the computer.
  """
  choices = ["Rock", "Paper", "Scissors"]

  print("Let's play Rock, Paper, Scissors!")

  user_choice = input("Enter your choice (R/P/S): ").upper()
  computer_choice = random.choice(choices)

  print(f"Computer chose: {computer_choice}")

  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "R" and computer_choice == "S") or \
       (user_choice == "P" and  computer_choice == "R") or \
       (user_choice == "S" and computer_choice == "P"):
    print("You win!")
  else:
    print("You lose!")

# Run the game
play_rock_paper_scissors()