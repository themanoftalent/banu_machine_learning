# this is about regex
import re

hand = open('shortez.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
    else:
        print('No match')

with open('shortez.txt') as f:
    for line in f:
        line = line.rstrip()
        if re.search('[a-zA-Z]\S*', line):
            print(line)
