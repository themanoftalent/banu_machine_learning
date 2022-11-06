# Guessing Games
counter: int = 0
num = 9

# import random

# num = random.randint(1, 10)
guess = None

while guess != num:
    try:
        guess = input("guess a number between 1 and 10: ")
        guess = int(guess)

    except ValueError:
        print("Numbers only")
    else:
        if guess == num:
            print("congratulations! you won!")
            break
        if guess <= 0 or guess > 10:
            print("Between 1 and 10")

        else:
            print("nope, sorry. try again!")

else:
    print("Finished")
