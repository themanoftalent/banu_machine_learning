from pathlib import Path
import os
import sys

#Absolute path
#c:\Program Files\Microsoft
# /usr/local/bin

#Relative path
# Path("ecommerce")
# Path("ecommerce/__init__.py")
# Path() / "ecommerce" / "__init__.py"

path= Path("ecmetin")
print(path.exists())

path=Path("emails")
print(path.exists())
# print(path.mkdir())
print(os.rmdir("emails"))
