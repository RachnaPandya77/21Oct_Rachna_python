# Write python program that swap two number with temp variable and without temp variable

# with temp

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swap : ", a)
print("After swap : ", b)

# without temp

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x,y = y,x

print("After swap : ", x)
print("After swap : ", y)

