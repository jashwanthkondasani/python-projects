# import random

# top_of_range=input("Type a number: ")
# if top_of_range.isdigit():
#     top_of_range=int(top_of_range)

#     if top_of_range<=0:
#         print("Please enter a number greater than 0.")
#         quit()
# else:
#     print("Please enter a valid number.")
#     quit()
import random

print("🎮 Welcome to the Number Guessing Game!")

number = random.randint(1, 100)   # Random number between 1 and 100
guesses = 0

while True:
    guess = input("Guess a number between 1 and 100: ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    guesses += 1

    if guess == number:
        print("🎉 Correct! You guessed it in", guesses, "attempts.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")