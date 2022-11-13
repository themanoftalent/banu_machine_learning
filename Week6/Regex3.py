import re

pattern = '^a...s$'
test_string = 'abbas'
result = re.match(pattern, test_string)

if result:
    print('Found a match!')
else:
    print("Search unsuccessful.")

# MetaCharacters
# Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:
#
# [] . ^ $ * + ? {} () \ |
#
# [] A set of characters

# Example
# Find a sequence that starts with "he", followed by two (any) characters, and an "o":

texting = "hello 123 world 456, howdy metto 789"
pattern = "\w\w\w\wo"
result = re.findall(pattern, texting)
print(result)

pattern = '\D+'
result = re.findall(pattern, texting)
print(result)

pattern = '\d+'
result = re.findall(pattern, texting)
print(result)

pattern = '\s'
result = re.findall(pattern, texting)
print(result)

pattern = '\S+'
result = re.findall(pattern, texting)
print(result)

pattern = 'h'
result = re.split(pattern, texting)
print(result)

string = 'One 1, Twelve:12 Eighty nine:89 Nine:9. Ten:10 Eleven:11'
pattern = '\d+'
result = re.split(pattern, string)
print(result)
