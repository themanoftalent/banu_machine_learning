import re

user_input = ''

while True:
    user_input = input('Enter letters only = ')
    if not re.match(r'^[a-zA-Z]+$',user_input):
        print("Letters only")
        continue
    else:
        print(user_input)
        break
