import random


def play_rps():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        # Get user choice and convert it to lowercase
        user_choice = input("\nChoose (rock, paper, scissors) or type 'quit' to exit: ").lower().strip()

        # Check if the user wants to quit
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break

        # Validate input
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie! 🤝")
        elif (
                (user_choice == "rock" and computer_choice == "scissors") or
                (user_choice == "paper" and computer_choice == "rock") or
                (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round! 🎉")
        else:
            print("Computer wins this round! 💻")

        print("-" * 40)


if __name__ == "__main__":
    play_rps()