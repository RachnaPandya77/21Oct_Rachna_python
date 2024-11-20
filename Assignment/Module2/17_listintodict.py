# Write a Python program to convert two lists into one dictionary using a for loop

list1 = ['id','Name', 'Subject']
list2 = [101, 'Rachna', 'Python']


mydict = {}
for i in range(len(list1)):
     mydict [list1[i]] = list2[i]
#mydict = list1 + list2

print(mydict)