#  Write a Python program to remove elements from a list using pop() and remove()

color = ['white','red','blue','green','pink']
print(color)

#pop
color.pop(1)
print("Remove 1 index value")
print(color)

color.pop()
print("remove last value")
print(color)


#remove
print("-----------------------------------------")
color1 = ['white','red','blue','green','pink']
color1.remove('green')

print(color1)