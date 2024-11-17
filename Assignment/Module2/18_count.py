# Write a Python program to count how many times each character appears in a string

mystring = "Heloo python"

stringcount = {}
for i in mystring:
    if i in stringcount:
        stringcount[i] += 1
    else:
        stringcount[i] = 1

print(stringcount)
