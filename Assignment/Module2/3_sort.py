# Write a Python program to sort a list using both sort() and sorted()

subject = ['php', 'c', 'c++', 'python']
print(subject)

subject.sort()
print("sorts element in ascending order: ",subject)

subject.sort(reverse=True)#print string in reverse order
print(subject)

print("---------------------------")

list1 = sorted(subject)
print(list1)

