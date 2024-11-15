# Write a Python program to access values using keys from a dictionary

mydict = {'id': 101, 'name':'Rachna','age': 24, 'city': 'Jetpur', 'country': 'India'}
print(mydict)

print(mydict['id'])
print(mydict.keys())
print(mydict.values())
print(mydict.items())

for i in mydict.items():
    print(i)