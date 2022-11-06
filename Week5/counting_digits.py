try:
    def countDigits(num):
        count = 0
        while True:
            num = num // 10
            count += 1
            if num == 0:
                break
            else:
                continue
        if count == 1:
            print("Ouch gotch it, it is 1")
        else:
            print("Number of digits: " + str(count))


    num = int(input('Enter numbers to be count '))
    if num == '-' or num == '=':
        print("Please enter a valid number, only numbers are allowed")

    countDigits(num)
except ValueError:
    print("Please enter a valid number, only numbers are allowed")
    num = int(input('Enter numbers to be count '))
    countDigits(num)
