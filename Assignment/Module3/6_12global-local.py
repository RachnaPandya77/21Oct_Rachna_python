"""Write a Python program to demonstrate the use of local and
global variables in a class.
"""

stu_nm = 'Rachna Pandya'#global var

class myclass:
    
    def getdata(self):
        print(stu_nm)

    def localdata(self):
        message = f"Hi {stu_nm}"  #local var
        print(message)

obj1 = myclass()
obj1.getdata()
obj1.localdata()