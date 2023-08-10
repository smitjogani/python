# to call super class constructer in sub class using super()

class Parent(object):
    def __init__(self,p_age):
        self.p_age = p_age
    def get_age(self):
        print("Parent age is ",self.p_age)
    
class Child(Parent):
    def __init__(self, p_age, c_age):
        super().__init__(p_age)
        self.c_age = c_age
    
    def get_age(self):
        super().get_age()
        print("Child age : ",self.c_age)

c = Child(40,15)
c.get_age()