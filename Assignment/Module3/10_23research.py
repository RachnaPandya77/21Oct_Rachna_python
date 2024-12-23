# Write a Python program to search for a word in a string using re.search()

import re

mystr = "This is re.search"

str = re.search('re.search',mystr)
print(str)

if str:
    print("True")
else:
    print("Error")
