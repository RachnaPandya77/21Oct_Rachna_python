# Write a Python program to match a word in a string using re.match()

import re

text = "match a word in a string using re.match"

txt = re.match('match',text)
print(txt)

if txt:
    print("True")
else:
    print("Error")