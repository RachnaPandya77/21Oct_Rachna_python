# Write a Python program to show multiple inheritance

#parent class
class person:
    def personinfo(self, pname, age):
        self.pname = pname
        self.age = age

    def showinfo(self):
        print("ID: ", self.pname)
        print("Name: ", self.age)

#parent class
class employee:
    def empinfo(self, empid, position):
        self.empid = empid
        self.position = position

    def showemp(self):
        print("Employee id: ", self.empid)
        print("Employee position: ", self.position)

#child class
class manager(person, employee):
    def setinfo(self, department):
        self.department = department  

    def showdetail(self):
        self.showinfo() #call fun from person
        self.showemp() # call fun from employee

        print("Department: ", self.department)

#create obj
mngr = manager()

#set detail using function
mngr.personinfo('Rachna', 24)  # call fun from person
mngr.empinfo('101', 'HR') # call fun from employee
mngr.setinfo('IT')  # call fun from manager

#display all detail (obj call method from manager)
mngr.showdetail() 