# Write a Python program to create a file and write a string into it

fl = open('3_file1.txt','w')

name = input("Enter name: ")
fl.write(f"Your name is {name}")