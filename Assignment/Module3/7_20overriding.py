# Write a Python program to show method overriding

class baseinfo:
    def display_info(self):
        print("subject info ")

class subjectinfo(baseinfo):
    def display_info(self,data):
        print("Subject id: ",data)

class subjectname(baseinfo):
    def display_info(self, data):
       print("Subject Name: ",data)

#create obj
b = baseinfo()
sub = subjectinfo()
s_name = subjectname()

#display info
b.display_info()
sub.display_info(111)
s_name.display_info('Django')