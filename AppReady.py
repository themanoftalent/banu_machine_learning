import os
from pathlib import Path

path = Path()
if path.exists():
    print("Path exists")
else:
    print("Path does not exist")

print(path.cwd())
print(path.home())
print(path.absolute())
print(path.is_dir())
print(path.is_file())
print(os.curdir)

if 'Week4' not in os.listdir():
    print(os.mkdir("Week4"))
else:
    print("Week4 already exists")
