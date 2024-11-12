# Write a Python program that manipulates and prints strings using various string methods

mystr = "THIS IS string METHOD"
print(mystr)
print("------------------------------")
print("lower....",mystr.lower())
print("upper....",mystr.upper())
print("caseflod....",mystr.casefold())#covert cap to small
print("capitalize....",mystr.capitalize())#first letter capital
print("strip....",mystr.strip())

print("\n")
str = "      THIS IS string METHOD"
print(str)
print("strip....",mystr.strip())#remove space
print("\n")

mystr1 = "This is python assignment python"
print(mystr1)
print("replace....",mystr1.replace('python','js'))
print("split....",mystr1.split())
print("Title....",mystr1.title())
print("count....",mystr1.count('python'))
print("count....",mystr1.count('t'))
print("Endswith....",mystr1.endswith('n'))
print("Endswith....",mystr1.endswith('a'))
print("startswith....",mystr1.startswith('T'))
print("startswith....",mystr1.startswith('t'))
print("index....",mystr1.index('h'))
print("find....",mystr1.index('p'))

print("\n")
mystr2 = "Hello"
print(mystr2)
print("isalpha....",mystr2.isalpha())
mystr3 = "Hello123"
print(mystr3)
print("isalpha....",mystr3.isalpha())

print("\n")
num = "9998887"
print(num)
print("isdigit....",num.isdigit())
num1 = "rp9998887"
print(num1)
print("isdigit....",num1.isdigit())

print("\n")
method3 = "python311"
print(method3)
print("isalnum.....",method3.isalnum())
method2 = "123456#"
print(method2)
print("isalnum.....",method2.isalnum())
method1 = "123456"
print(method1)
print("isalnum.....",method1.isalnum())
method = "python"
print(method)
print("isalnum.....",method.isalnum())
email = "rp11@gmail.com"
print(email)
print("isalnum.....",email.isalnum())

print("\n")
lower = "hello python"
print(lower)
print("islower....", lower.islower())
lower1 = "Hello Python"
print(lower1)
print("islower....", lower1.islower())

print("\n")
upper = "PYTHON"
print(upper)
print("isupper....", upper.isupper())
upper1 = "Python"
print(upper1)
print("isupper....", upper1.isupper())




