import random

def guessing_game():
    # List of words for the game
    words = ["python", "programming", "computer", "algorithm", "code", "developer", "variable", "function", "loop", "debug"]

    # Select a random word from the list
    secret_word = random.choice(words)
    attempts = 0
    guessed_letters = []

    print("Welcome to the Word Guessing Game!")
    print("I've selected a word. Can you guess it?")

    while True:
        # Display the word with underscores for unguessed letters
        display_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print("Word:", display_word)

        guess = input("Enter a letter or guess the word: ").lower()
        attempts += 1

        if guess == secret_word:
            print(f"Congratulations! You've guessed the word '{secret_word}' correctly in {attempts} attempts!")
            break
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
        else:
            print("Invalid input. Please enter a single letter or guess the entire word.")

# Run the guessing game
guessing_game()
