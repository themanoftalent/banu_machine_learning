import re

txt = "The rain in Italy, then it will go through Spain"

findX = re.findall('a[i]n', txt)
print(findX)

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:
#
# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# RegEx Metacharacters
# Metacharacters are characters with a special meaning:
#
# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group

# RegEx Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
#
# Set	Description	Example	Try it
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present	"[arn]"
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	"[a-n]"
# [^arn]	Returns a match for any character EXCEPT a, r, and n	"[^arn]"
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	"[0123]"
# [0-9]	Returns a match for any digit between 0 and 9	"[0-9]"
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	"[0-5][0-9]"
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	"[a-zA-Z]"
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	"[+]"
# [^0-9]	Returns a match for any character that is not a digit

# RegEx Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#
# Sequence	Description	Example	Try it
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# RegEx Modifiers
# Modifiers are used to change the way search works:
#
# Modifier	Description	Example	Try it
# { }	Quantifier	"a{1,3}"	Returns a match for a string that contains from 1 to 3 "a" characters
# +	Checks for one or more characters to its left	"i+"	Returns a match for each position where the string contains one or more "i" characters
# ?	Checks for zero or one characters to its left	"i?"	Returns a match for each position where the string contains zero or one "i" characters
# *	Checks for zero or more characters to its left	"i*"	Returns a match for each position where the string contains zero or more "i" characters
# $	Checks for a match at the end of a string	"Spain$"	Returns a match if the specified characters are at the end of the string
# ^	Checks for a match at the beginning of a string that contains multiple lines, and in each line	"^The"	Returns a match if the specified characters are at the beginning of the string
# |	Alternation	"falls|stays"	Returns a match where one of the specified words (falls or stays) are present
# ()	Capture and group

