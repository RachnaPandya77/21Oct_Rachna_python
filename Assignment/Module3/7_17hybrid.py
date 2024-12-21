# Write a Python program to show hybrid inheritance

class medicine:
    def set_shopinfo(self, shopname, location):
        self.shopname = shopname
        self.location = location

    def show_shopinfo(self):
        print("shop name : ", self.shopname)
        print("shop location : ", self.location)

class person:
    def set_personinfo(self, pname):
        self.pname = pname
        

    def show_personinfo(self):
        print("person name : ", self.pname)
        
class customer(medicine,person):
    def set_customer(self, buymedicine):
        self.buymedicine = buymedicine

    def show_customer(self):
        self.show_shopinfo()
        self.show_personinfo()
        print("purchsed medicine: ", self.buymedicine)

c = customer()
c.set_shopinfo("Healthy pharmacy", "Rajkot")
c.set_personinfo("Rachna Pandya")
c.set_customer("NAM COLD")
print("--------Detail-----------")
c.show_customer()