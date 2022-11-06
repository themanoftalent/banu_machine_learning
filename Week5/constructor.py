# class User:
#     name = ""
#
#     def __init__(self, name):
#         self.name = name
#
#     def sayHello(self):
#         print("Welcome , " + self.name)
#
#     def goOut(self,leave):
#         print('Bye bye,go hell', leave)
#
#     def comeAgaoin(self,comeback):
#         print('Come please,', comeback)
#
#     def eatSth(self,hung):
#         print('Eat something,', hung)
#
# User1 = User("Melik")
# User1.sayHello()
# User1.goOut('man')
# User1.comeAgaoin('We can not leave without you')
# User1.eatSth('once')
# print('*'*23)
# User2 = User("Cemre")
# User2.sayHello()
# User2.goOut('girl')
# User2.comeAgaoin('Anyone can leave without you')
# User2.eatSth('once')

class Kullanici:
    name = ''

    # maas = ''

    def __init__(self, name):
        self.name = name
        print (name, end=',')

    def goOutMan(self, hayden, salary, age):
        self.hayden = hayden
        self.maas = salary
        self.age = age
        print ('hayden namaza', hayden, 'maasin', salary, ',', 'age is', age, '.')

    def eatOut(self, hayden, salary, age):
        self.hayden = hayden
        self.maas = salary
        self.age = age
        print ('avruoada', hayden, 'kacasin', salary, ',', 'taami ', age, '.')


kullanici1 = Kullanici ('malik')
kullanici1.goOutMan ('kos', 1500, 76)
kullanici1.eatOut ('aptal', 2, 3)

kullanici2 = Kullanici ('Ahmet')
kullanici2.goOutMan ('run', 1000, 38)
kullanici2.eatOut ('saf', 2, 3)

kullanici3 = Kullanici ('Cem')
kullanici1.goOutMan ('kos', 1500, 76)
kullanici3.eatOut ('Ne guzel', 33, 4)

kullanici4 = Kullanici ('Hulya')
kullanici4.goOutMan ('run', 1000, 38)
kullanici4.eatOut ('Oha', 76, 44)
