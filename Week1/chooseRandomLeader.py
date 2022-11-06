# import random
#
#
# def randomChoosers():
#     friends = ['Akif', 'Mehmet', 'Musa', 'Isa', 'Haluk', 'Zeynep', 'Bekant', 'Gozde', 'Selma', 'Nisa']
#     # for i in range(len(friends)):
#     #     print(random.choice(friends[i]))
#     for i in friends:
#         return random.choice([i])
#
#
# print(randomChoosers())


import random


def randomChoosers():
    f = open("liderler.txt", 'r', encoding='utf-8')
    for i in enumerate(list(f.readlines())):
        return random.choice(i)


print(randomChoosers())
