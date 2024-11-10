# Write a Python program to check if a number is positive, negative or zero

num = int(input("Enter a number: "))

if num < 0:
    print("Number is negative")
elif num == 0:
    print("It is Zero")
else:
    print("Number is positive")