import random


def choose_difficulty():
    """Let the player choose a difficulty level."""
    print("\nChoose difficulty:")
    print("1. Easy - 10 attempts")
    print("2. Medium - 7 attempts")
    print("3. Hard - 5 attempts")

    while True:
        difficulty = input("Choose 1, 2, or 3: ").strip()

        if difficulty == "1":
            return "Easy", 10, 5
        elif difficulty == "2":
            return "Medium", 7, 10
        elif difficulty == "3":
            return "Hard", 5, 20
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def get_guess():
    """Get and validate the player's guess."""
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game():
    """Run one round of the guessing game."""
    secret_number = random.randint(1, 100)

    difficulty, max_attempts, penalty = choose_difficulty()

    score = 100
    attempts = 0

    print(f"\nDifficulty: {difficulty}")
    print(f"You have {max_attempts} attempts.")
    print(f"Starting score: {score}")

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if guess == secret_number:
            print("\n🎉 Correct!")
            print(f"The number was {secret_number}.")
            print(f"Attempts used: {attempts}")
            print(f"Final score: {score}")
            return

        score = max(0, score - penalty)

        if guess > secret_number:
            print("Too High!")
        else:
            print("Too Low!")

        print(f"Attempts remaining: {max_attempts - attempts}")
        print(f"Current score: {score}")

    print("\nGame Over!")
    print(f"The secret number was: {secret_number}")
    print(f"Final score: {score}")


def main():
    """Start and control the game."""
    print("============================")
    print("     NUMBER GUESSING GAME")
    print("============================")

    while True:
        play_game()

        while True:
            play_again = input(
                "\nWould you like to play again? (y/n): "
            ).strip().lower()

            if play_again == "y":
                print("\nStarting a new game...")
                break

            elif play_again == "n":
                print("\nThanks for playing!")
                print("Goodbye!")
                return

            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()

