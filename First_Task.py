# Guess the Number Game - Beginner Version

import random

print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 10.")
print("You have 3 chances to guess the number.")

# Random number between 1 to 10
secret_number = random.randint(1, 10)

# Set attempts
attempts = 3

# Start guessing
while attempts > 0:
    guess = input("Enter your guess: ")
    guess = int(guess)

    if guess == secret_number:
        print("You got it right! 🎉")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts = attempts - 1
    print("Attempts left:", attempts)

if guess != secret_number:
    print("Sorry, you lost! 😢 The number was", secret_number)
