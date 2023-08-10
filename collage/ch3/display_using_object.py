class Employee:
    def __init__(self):
        self.name = 'Smit Jogani'
        self.age = 19
        self.salary = 5000
    
    def display(self):
        print("Hello! My name is ",self.name)
        print("My age is ",self.age)
        print("My salary is ",self.salary)
    
e = Employee()
e.display()