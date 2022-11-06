class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, This is {self.name}. He wants you go ")  # self. name demek lazım

    def move(self):
        print(f"{self.name} is moving.")


person = Person("John Smith")
person.talk()
person.move()


person2 = Person("Bob Smith")
person2.talk()
person2.move()
