num = 0

while True:
    try:
        num = int(input("Enter an integer 1-5: "))
    except ValueError:
        print("Please enter a valid integer 1-5")
        continue
    if num >= 1 and num <= 5:
        print(f'You entered: {num}')
        break
    else:
        print('The integer must be in the range 1-5')
    print("Do ou want to continue")
    answer = input("Enter y or n: ")
    if answer == "n":

