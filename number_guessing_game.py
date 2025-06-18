# number_guessing_game.py

import random

print("🎯 Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Let the user guess up to 3 times
for attempt in range(3):
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
        break
    else:
        print("❌ Nope! Try again.")
else:
    print(f"😞 Sorry! The number was {secret_number}.")

input("\nPress Enter to exit...")

