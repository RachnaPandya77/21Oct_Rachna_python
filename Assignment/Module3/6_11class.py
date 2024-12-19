"""Write a Python program to create a class and access the properties
of the class using an object"""

class employee:
    name = 'Rachna'
    city = 'Rajkot'

    def getdata(self):
        print("This is employee class")

emp = employee()
print("ID: ",emp.name)
print("Name: ",emp.city)

emp.getdata()

