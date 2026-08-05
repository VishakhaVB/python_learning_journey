import random

n = random.randint(1, 100)
a = -1
guess = 0

while a != n:
    guess += 1
    a = int(input("Enter a number: "))

    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print(f"You guessed it right! The number was {n}.")
        print(f"It took you {guess} attempts.")