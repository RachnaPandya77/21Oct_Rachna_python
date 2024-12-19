# Write a Python program to show multilevel inheritance

class animal:
    def speak(self):
        print(f"{self.speak} makes a sound")

class dog(animal):
    def bark(self):
        print(f"{self.bark} barks")