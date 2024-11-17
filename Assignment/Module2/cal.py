# Write a Python program to create a calculator using functions

n1 = int(input("Enter num: "))
n2 = int(input("Enter num: "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

choice = int(input("Enter choice (1 to 4): "))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if choice == 1:
    print("Sum : ", add(n1,n2))

elif choice == 2:
    print("Sub: ", sub(n1,n2))

elif choice == 3:
    print("Mul: ", mul(n1,n2))

elif choice == 4:
    print("Div: ", div(n1,n2))

else:
    print("Enter valid choice")




