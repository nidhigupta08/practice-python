import random

lower_bound = 1
upper_bound = 100
number_to_guess = random.randint(lower_bound, upper_bound)
attempts = 0

print(f"Guess the number between {lower_bound} and {upper_bound}")

while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        break
