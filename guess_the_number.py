import random

guess = int(
    input("I'm thinking of a number from one to 100, can you guess what it is? "))

num_of_tries = 1
computer_guess = random.randint(0, 100)
while guess is not computer_guess:
    num_of_tries += 1
    if guess < computer_guess:
        print("higher!")
    elif guess > computer_guess:
        print("lower!")
    guess = int(input("Try again "))

print("nice, it took you", num_of_tries, "tries")
