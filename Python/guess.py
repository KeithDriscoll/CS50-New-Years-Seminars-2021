import random

number = random.randint(1, 10)

for i in range(3):
    x = int(input("Guess a number between 1 and 10: "))
    if x == number:
        print("Correct!")
        break
    else:
        print("That's not correct!")