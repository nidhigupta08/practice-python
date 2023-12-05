import random

def hangman():
    words = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry", "blueberry"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display = ''.join(letter if letter in guessed_letters else '_ ' for letter in secret_word)
        print(display)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word correctly.")
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess not in secret_word:
            print("Wrong guess!")
            attempts -= 1
            guessed_letters.append(guess)
        else:
            guessed_letters.append(guess)

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{secret_word}'.")

hangman()
