"""Create a mini-project where students combine conditional statements, loops, 
and functionsto create a basic Python application, such as a simple calculator
or a grade management system. """

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))

print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
choice = int(input("Enter choice(1 to 4): "))

if choice == 1:
    print("Add: ", n1 + n2)
elif choice == 2:
    print("Sub: ",n1 - n2)
elif choice == 3:
    print("Mul: ", n1 * n2)
elif choice == 4:
    print("Div: ", n1 / n2)
else :
    print("Enter valid choice")








