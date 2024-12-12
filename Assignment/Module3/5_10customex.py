# Write a Python program to print custom exceptions

try:
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))

    if b == 0:
        raise ValueError("division not allowed")
    
    result = a / b
    print("result: ",result)

except Exception as e:
    print(e)