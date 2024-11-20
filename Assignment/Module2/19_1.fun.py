# Write a Python program to create a calculator using functions

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
choice = int(input("Enter a choice: "))

a = x + y
s = x - y
m = x * y
d = x / y

def add():
    print("add: ",a)

def sub():
    print("sub: ",s)
   
def mul():
    print("mul: ", m)

def div():
    print("div: ", d)

if choice == 1 :
    add()

elif choice == 2:
    sub()

elif choice == 3:
    mul()

elif choice == 4:
    div()

else:
    print("Enter valid choice")
    








