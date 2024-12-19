# Write a Python program to show single inheritance

class myclass:
    name:str
    age:int
    city:str

    def getdata(self):
        self.name=input("Enter Your Name: ")
        self.age=input("Enter Your Age: ")
        self.city=input("Enter city: ")

class info(myclass):
    def showdata(self):
        print(f"Student Info:\n{{'name': '{self.name}', 'age': {self.age}, 'city': '{self.city}'}}")

st = info()
st.getdata()
st.showdata()

