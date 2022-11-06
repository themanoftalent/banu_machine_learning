try:
    age = int(input("Enter some value integer = "))
    income = 20000
    riking = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero.")
except ValueError:
    print("Only digits, characters are not allowed.")
