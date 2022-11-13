# Program to remove all whitespaces

import re


def main():
    # Get a string from the user
    s = input("Enter a string: ")

    # Remove all whitespaces
    s = re.sub(r"\s", "", s)

    # Display the string
    print("The string with no whitespaces is", s)


x = main()
print(x)






