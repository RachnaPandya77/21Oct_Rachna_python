# Write a Python program to show method overloading

class info:
    def display_info(self, id):
        print("Subject ID: ", id)

    def display_info(self,name):
        print("Sub Name: ",name)

obj = info()
obj.display_info('Python')
obj.display_info(123)
