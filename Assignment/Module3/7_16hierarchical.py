# Write a Python program to show hierarchical inheritance

#parent class
class college:
    def set_clginfo(self, clgname, location):
        self.clgname = clgname
        self.location = location

    def show_clginfo(self):
        print("College Name: ",self.clgname)
        print("Location: ",self.location)

#child class
class student(college):
    def set_stdinfo(self, stdname, stdid):
        self.stdname = stdname
        self.stdid = stdid

    def show_stdinfo(self):
        self.show_clginfo()
        print("Student Name: ",self.stdname)
        print("Student ID: ", self.stdid)

#child class
class faculty(college):
    def set_facultyinfo(self, f_name, f_id, subject):
        self.f_name = f_name
        self.f_id = f_id
        self.subject = subject

    def show_facultyinfo(self):
        self.show_clginfo()
        print("Faculty Name: ", self.f_name)
        print("Faculty ID: ", self.f_id)
        print("Subject: ", self.subject)

#object create for student
std = student()
std.set_clginfo("Tops Technology", "Rajkot")
std.set_stdinfo("Rachna Pandya", "101")
std.show_stdinfo()

print("---------------------------------------")

#obj for faculty
f = faculty()
f.set_clginfo("Tops Technology", "Rajkot")
f.set_facultyinfo("Sanket sir", "s111", "Python")
f.show_facultyinfo()


    