"""Write a Python program to handle file exceptions and use the finally block for closing
the file"""

final_file = "data.txt"

try:
    file = open(final_file, 'r')
    data = file.read()

    print("File data: ",data)

except FileNotFoundError as e:
    print("file not found")

finally:
    file.close()
    print("file close")