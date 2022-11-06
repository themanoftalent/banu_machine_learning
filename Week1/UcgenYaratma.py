numbers = [2, 2, 3, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12, 13, 124, 564, 876, -123, 56, 45, 78, 34, 77]
uniques = []

for number in numbers:
    if number in uniques:
        continue
    else:
        uniques.append(number)
        print(number, uniques)
