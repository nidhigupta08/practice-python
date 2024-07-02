import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while True:
        print("\nAttempts left:", max_attempts - attempts)
        guess = int(input("Enter your guess: "))

        attempts += 1

        # Check if the guess is correct
        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break

        # Check if the player has used all attempts
        if attempts == max_attempts:
            print(f"\nSorry, you've run out of attempts. The number was {secret_number}.")
            break

    print("\nGame Over")

# Run the game
guess_number_game()
