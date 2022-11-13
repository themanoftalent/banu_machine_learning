# finding average
class matematika:  # find average
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def average(self):
        return (self.a + self.b + self.c + self.d + self.e) / 5

    def __str__(self):
        return "The average is: " + str(self.average())


intputting = int(input("How many numbers you want to average?"))
if intputting == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(matematika(a, b, 0, 0, 0))
elif intputting == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(matematika(a, b, c, 0, 0))
elif intputting == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))
    print(matematika(a, b, c, d, 0))
elif intputting == 5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))
    e = int(input("Enter fifth number: "))
    print(matematika(a, b, c, d, e))
else:
    print("You can only average 2-5 numbers")
