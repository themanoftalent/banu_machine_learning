import random


# n = int(input('Enter a random number :'))
# for i in range(n):
#         print(random.randint(i,100))


########################################################################
# n = int(input('Enter a random number '))
# for i in range(n):
#     print(random.random())
##     print(random.random(10,20))

def randomGir(x):
    sayiTut = []
    try:
        for i in range(x):
            if i != 4:
                if not i in sayiTut:
                    sayiTut.append(i)
                    print(random.random())
                elif i >= 23:
                    print(random.gauss())
                else:
                    print(random.randint())
        return i

    except ValueError:
        print("Something gone wild")


x = int(input('Enter a random number '))

randomGir(x)
