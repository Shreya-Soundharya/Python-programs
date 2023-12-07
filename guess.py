#Guessing game

import random

def guessing_game():
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the guessing game!")
    print("I've selected a random number between 1 and 100.")

    while True:
        try:
            user_guess = int(input("Guess the number: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
