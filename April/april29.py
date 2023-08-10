# Creating a class instance

class Employee:
    salutation = "Wel-Come"  # class instenceattributes

    def __init__(self):
        self.name = 'Smit'
        self.id = '1'

    def display(self):  # class instance method
        print(f"Employee name is {self.name} and id is {self.id}")


emp = Employee()  # object of class

print(emp.salutation)  # call instance attributes
emp.display()  # call instance attributes
