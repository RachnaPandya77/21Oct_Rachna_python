# Write a Python program to check the current position of the file cursor using tell()

myfile = '3_file1.txt'

file = open(myfile,'r')
file.read()

c_position = file.tell()
print("current position of cursor: ",c_position)

