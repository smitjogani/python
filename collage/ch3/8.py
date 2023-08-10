# cerate employee class and make all the members of the employee class avalable to another class by passing members of one class to another

class Emp:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("Id     ", self.id)
        print("Name   ", self.name)
        print("Salary ", self.salary)

class MyClass:
    @staticmethod
    def myMethod(e):
        e.salary += 1000
        e.display()

e = Emp(10, "Smit Jogani", 15000)
MyClass.myMethod(e)