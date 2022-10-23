num = 0
secretnumber = 3
while True:
    try:
        num = int(input("Enter an integer 1-5: "))
    except ValueError:
        print("Please enter a valid integer 1-5")
        continue
    if num >= 1 and num <= 5:
        break
    else:
        print('The integer must be in the range 1-5')

if num == secretnumber:
    print('You won! the guess is {0}'.format(secretnumber))

else:
    print(f'Wrong, you failed. The number entered is: {num}')
