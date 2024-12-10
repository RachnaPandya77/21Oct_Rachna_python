# Write a Python program to write multiple strings into a file

str1 = ['Python is a user-friendly programming language', 
        'Python supports modules and packages',
        'Python is an interpreted, object-oriented programming language']

f1 = open('4_mulstr.txt','w')
for i in str1:
    f1.write(i + "\n")

print("Your file is ready")
