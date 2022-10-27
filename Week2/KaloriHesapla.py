class Kalori_Calculator:
    def __init__(self, carbs, fat, protein):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein

    def calculate(self):
        calories = self.carbs * 4 + self.fat * 9 + self.protein * 4
        return calories


carbs = int(input("How many carbohydrates does this product have?: "))
fat = int(input("How much fat does this product have?: "))
protein = int(input("How much protein does this product have?: "))

myCal = Kalori_Calculator(carbs, fat, protein)
print(myCal.calculate())

print("################ Yag Hesaple ###################" * 1)


class Yag_hesapla(Kalori_Calculator):
    def __init__(self, fat):
        self.fat = fat

    def calculate(self):
        calories = self.fat * 9
        return calories

    def calculate(self):
        calories = self.fat * 9
        return calories


yag = int(input("Ne kadar yag yersin: "))
seninYag = Yag_hesapla(yag)
print(seninYag.calculate())
