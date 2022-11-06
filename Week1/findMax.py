numbers = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 124, 564, 876, -123, 56, 45, 78, 34, 77]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)
