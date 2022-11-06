# class Dog:
#
#     def __init__(self,name):
#         self.name = name
#
#
#     def walk(self):
#         print("Walk")
#
#
# #DRY DONT REPEAT YOURSELF
#
# class Cat:
#
#     def __init__(self, name):
#         self.name=name
#
#     def walk(self):
#         print("Walk")

#### class inheritence ####
class Mammal:
    def __init__(self, name):
        self.name = name
        print("Easy boy", name)

    def walk(self):
        print(f"{self.name} walk")


class Dog(Mammal):

    def bark(self):
        print("bark")


class Cat(Mammal):
    def miyaw(self):
        print("miyaw")


dog1 = Dog("Barny")
dog1.walk()
dog1.bark()
print("####################")
cat1 = Cat("Katy")
cat1.walk()
cat1.miyaw()
