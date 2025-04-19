import random

# It's a number guessing game

# Game Rules
print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 chances to guess the correct number.")

# Game Logic using conditionals
number_to_guess = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Enter your guess: "))
    
    if guess == number_to_guess:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < number_to_guess:
        print("📉 Too low!")
    else:
        print("📈 Too high!")
    
    attempts -= 1
    print(f"❗ Attempts left: {attempts}")

# End of game
if attempts == 0 and guess != number_to_guess:
    print(f"😢 Sorry! The correct number was {number_to_guess}. Better luck next time!")
