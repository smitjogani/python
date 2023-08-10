# constructer having more than one parameter

class Student:
    def __init__(self, name = " ", m = 0):
        self.name = name
        self.marks = m
    
    def display(self):
        print(f"Hi My name is {self.name}")
        print(f"Marks : {self.marks}")

s = Student()
s.display()
print("-----------\n")

s1 = Student("Smit", 100)
s1.display()