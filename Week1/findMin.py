numbers = [2, 3, 5, 6, 7, 8, 9, 10, 11, -348, 12, 13, 124, 564, 876, -123, 56, 45, 78, 34, 77]
min_numbers = numbers[0]
for i in numbers:
    if i < min_numbers:
        min_numbers = i
print(min_numbers)
