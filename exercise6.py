import random

guess_correct = False
number_to_guess = random.randint(1, 9)

while not guess_correct:

    guess = int(input("Guess the Number (1-9)\n"))

    if guess == number_to_guess:
        print("You won!")
        exit(0)
    elif guess > number_to_guess:
        print("Too high!")
    elif guess < number_to_guess:
        print("Too low!")