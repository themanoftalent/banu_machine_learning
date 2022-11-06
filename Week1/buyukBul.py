def find_max(numbers):
    maximum = numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
    return maximum


# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 15, 67]
# print(find_max(numbers))
