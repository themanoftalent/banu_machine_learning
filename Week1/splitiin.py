# message = input('>')
# words = message.split(' ')
# print(words)

from pathlib import Path
import os

path = Path("ecommerce")
print(path.exists())
if path.exists():
    print('yes exists')
else:
    print(os.mkdir("WeekRegex"))
print("here we listed the files=")
print(os.listdir())
print("here we search the files=")
# print(path.glob('*.*')) #<generator object Path.glob at 0x104b0bbc0>

for file in path.glob('*.*'):
    print(file)
