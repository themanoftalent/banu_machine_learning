lowerCase = "GO FROM ZERO TO HERO WITH PYTHON."

if len(lowerCase) > 51:
    print('A paragraph')
elif len(lowerCase) == 50:
    print('That is correct')

else:
    print("Try other options")

print(len(lowerCase))

checkIt = " go" in lowerCase
print(checkIt)
