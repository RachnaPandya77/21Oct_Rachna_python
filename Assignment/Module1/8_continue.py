# 1. Write a Python program to skip 'banana' in a list using the continue statement
# List1 = ['apple', 'banana', 'mango']

list1 = ['apple','banana','mango']

for fruits in list1:
    if fruits == 'banana':
        continue
    print(fruits)