# create student class and display() 

class Student:
    def __init__(self):
        self.name = "smit"
        self.age = 19
        self.marks = 89
    
    def display(self):
        print(f"Hi My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"Marks : {self.marks}")
    
s1 = Student()
s1.display()