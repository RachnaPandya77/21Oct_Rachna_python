# Write a Python program to merge two lists into one dictionary using a loop

list1 = ['H:','C:','J:']
list2 = ['HTML','CSS','JS']

print("This is merged list: ", list1 + list2)

dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]

print("This is merged dict in key and values : ", dict1)