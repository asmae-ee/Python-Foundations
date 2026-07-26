import random


def word_guessing_game():
    # 1. Available word bank in English
    words = ["python", "programming", "computer", "intelligence", "developer", "software"]

    # Choose a random secret word
    secret_word = random.choice(words)

    # Initialize basic variables
    guessed_letters = []
    attempts = 6  # Allowed wrong attempts

    print("Welcome to the Word Guessing Game!")
    print(f"You have {attempts} allowed wrong attempts.")

    while attempts > 0:
        # Display the word with spaces and underscores
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nWord: {display_word.strip()}")

        # Check if the player has guessed all letters
        if "_" not in display_word:
            print("Congratulations! You won and guessed the word successfully 🎉")
            break

        # Ask the user for a letter input
        guess = input("Guess a single letter: ").lower().strip()

        # Validate the input (single letter only)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        # Add the letter to the guessed list
        guessed_letters.append(guess)

        # Check if the letter is in the secret word
        if guess in secret_word:
            print(f"Great! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong! The letter is not in the word. Remaining attempts: {attempts}")

    else:
        # Executed if attempts run out (Loss)
        print(f"\nOut of attempts! You lost. The correct word was: {secret_word}")


if __name__ == "__main__":
    word_guessing_game()