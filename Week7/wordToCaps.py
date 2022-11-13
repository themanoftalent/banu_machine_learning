# this programm turns input into all caps

class WordToCaps:

    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word

    def __add__(self, other):
        return self.word + other

    def __radd__(self, other):
        return other + self.word

    def capallLetters():
        word = input("Enter a word: ")
        print(word.upper())
        print(word)
        print(repr(word))
        print(word + "!")
        print("!" + word)

    def FirstLetterCap():
        word = input("Enter a word: ")
        print(word.capitalize())


capallLetters = WordToCaps.capallLetters()
capFirst = WordToCaps.FirstLetterCap()
