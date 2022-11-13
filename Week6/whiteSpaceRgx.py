import re

txt = "The rain in  Italy falls mainly in the plain! "
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
print("The second white-space character is located in position:", x.end())
