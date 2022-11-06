# themanoftalent

class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # return name, age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Cat(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.age} years old and {self.color}"

    def speak(self, sound="Meow"):
        return f"{self.name} says {sound}"


class Dog(Animals):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"


godo = Dog("Godo", 5)
print(godo.speak())
print(godo)

print()
print()

fido = Cat("Fido", 5, "brown")
print(fido)
print(fido.speak())
print(fido.name)
print(fido.color)
print(fido.age)
