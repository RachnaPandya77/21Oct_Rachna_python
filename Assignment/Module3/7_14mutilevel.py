# Write a Python program to show multilevel inheritance

class Fruit:
    def set_detail(self, name, color):
        self.name = name
        self.color = color

    def show_fdetail(self):
        print(f"Fruit name: {self.name}")
        print(f"Fruit color: {self.color}")

class Mango(Fruit):
    def has_vitamin(self, v_name):
        self.v_name = v_name

    def show_mdetail(self):
        super().show_fdetail()  
        print(f"Vitamin in mango: {self.v_name}")

class Orange(Mango):
    def set_detail(self, name, color):  
        super().set_detail(name, color)  

    def show_odetail(self):
        super().show_fdetail() 

# Objects
f = Fruit()
f.set_detail('Apple', 'Red')

m = Mango()
m.set_detail('Mango', 'Yellow')
m.has_vitamin('Yes')

o = Orange()
o.set_detail('Orange', 'Orange')

# Show details
print("Fruit details:")
f.show_fdetail()
print("\nMango details:")
m.show_mdetail()
print("\nOrange details:")
o.show_odetail()
