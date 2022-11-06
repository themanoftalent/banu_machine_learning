fruits = ["apple", "orange", "kiwi", "melon", "lemon"]

for fruit in fruits:
    if fruit.startswith("a") or fruit.startswith("o"):
        print(fruit)
    else:
        print('################################################################')
        print(fruit, "doesn't match")

fruits2 = ["cherry", "berry", "ananas", "reens", "lemonade"]

print('################################################################')
fruitAll = fruits2 + (fruits)
for fruited in zip(fruitAll):
    pass

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()

print(guests)
################################################################

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print('################################################################')
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print('################################################################')

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575,
    219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894,
    767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328,
    753, 470, 743, 527 ]


# your code goes here
for number in numbers:
    if isinstance(number, int):
        print("is istance of ",number)
        break
print("################################################################")
for i in numbers:
    if i % 2 == 0:
        print('When  modulo ',i)
        break
