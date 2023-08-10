# write a program to access the base class constructor from a sub class by using super() method and also without using super() method

'''
class Father:
    def __init__(self):
        self.property = 100000
    
    def display(self):
        print("Father's Property : ", self.property)
    
class Son(Father):
    pass

s = Son()
s.display()
'''

# with super()
class Father:
    def __init__(self, fproperty = 0):
        self.fproperty = fproperty

    def display(self):
        print("Father's Property : ", self.property)

class Son(Father):
    def __init__(self,sproperty,fproperty):
        super().__init__(fproperty)
        self.sproperty = sproperty
    
    def display(self):
        print("Son's Property : ", self.sproperty)
        print("Son's total Property : ", self.fproperty + self.sproperty)

s = Son(100000,50000)
s.display()