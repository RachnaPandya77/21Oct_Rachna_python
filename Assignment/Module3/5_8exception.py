#Write a Python program to handle multiple exceptions(e.g., file not found, division by zero)

file1 = '4_mulstr.txt'
try: 
    file = open(file1,'r')
    content = file.read()

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

    print('File content : ',content)
    print('result of division: ',result)

except FileNotFoundError as e:
    print("File not found")

except ZeroDivisionError as e:
    print("Division by zero error")

except Exception as e:
    print(e)