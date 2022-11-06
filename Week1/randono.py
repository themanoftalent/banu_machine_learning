import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        first = random.randint(1, self.sides)
        second = random.randint(1, self.sides)
        return first, second

dice1=Dice(6)
print(dice1.roll())

dice2=Dice(6)
print(dice2.roll())
