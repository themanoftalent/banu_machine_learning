# this will split the string into a list of words

import re

txt = "The rain in Italy falls mainly in the plain"
x = re.split("\s", txt)
print(x)

x1 = re.split("\s", txt, 1)
print(x1)

x2 = re.sub("\s", "9", txt)
print(x2)
