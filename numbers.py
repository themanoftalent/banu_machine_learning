x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print("#########"*4)

x1 = 1.10
y1 = 1.0
z1 = -35.59

print(type(x1))
print(type(y1))
print(type(z1))

print("#########"*4)

x3 = 3+5j
y3 = 5j
z3 = -5j

print(type(x3))
print(type(y3))
print(type(z3))

print("#########"*4)
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("#########"*4)

# lets import math
import math

print('Math floor ',math.floor(2.3))
print("math ceil ",math.ceil(2.6))
print("math power ",math.pow(11,2))

integer = -3.29
print('Absolute value of -20 is:', abs(integer))
print("Math Absolute value of -20 is:", math.fabs(integer))

#Import the random module, and display a random number between 1 and 9:
print("#########"*4)

import random

print(random.randrange(1,10))
