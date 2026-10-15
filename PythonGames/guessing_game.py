
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n================================")
    print("     NUMBER GUESSING GAME")
    print("================================")
    print("I have selected a number from 1 to 100.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You won!")
                print(f"The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                print(f"Your score: {max(0, 100 - (attempts - 1) * 10)}")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("\nThanks for playing. Goodbye!")
        break
