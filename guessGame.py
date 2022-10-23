secret_number = 156
guess_count = 0
while guess_count < 5:
    try:
        guess = int(input("Enter secret number: "))
        guess_count= guess_count + 1

    except ValueError:
        print("Invalid characters, only numbers")
    else:
        if guess == secret_number:
            print("Secret number is correct")
            break
        else:
            print("Secret number is incorrect")


