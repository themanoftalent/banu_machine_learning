# restrict o letters only
user_input = ''
while True:
    user_input = input('Enter letters only = ')

    if not user_input.isalpha():
        print('Enter letters only')
        continue
    else:
        print(user_input)
        break

