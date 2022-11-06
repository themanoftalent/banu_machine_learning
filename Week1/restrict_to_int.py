# input a number
while True:
    try:
        num = int(input("Enter an integer number: "))
        break
    except ValueError:
        print("Please input integer only...")
        continue
print("num:", num)
