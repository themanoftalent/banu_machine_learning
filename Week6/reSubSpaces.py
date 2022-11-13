#remoing extra spaces, no matter how many spaces are there
# it will format it into one space between words

import re


def reSubSpaces():
    inputting = input("Enter a string: ")
    print(re.sub(r'\s+', ' ', inputting))


reSubSpaces()
