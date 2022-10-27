class InfIter:

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        number = self.number
        self.number += 2
        return number


myIter1 = iter(InfIter())
print(next(myIter1))
