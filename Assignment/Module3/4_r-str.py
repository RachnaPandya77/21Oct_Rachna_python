"""Write a Python program to create a file and print the string into the
file."""

fl = open('4_file2.py','w')

str1 = input("Enter string : ")
fl.write(str1)