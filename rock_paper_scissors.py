import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Get the user's choice
user_choice = input("Enter your choice (rock, paper, or scissors): ")

# Get the computer's choice
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
  print("Tie!")
elif user_choice == "rock" and computer_choice == "scissors":
  print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
  print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
  print("You win!")
else:
  print("You lose!")