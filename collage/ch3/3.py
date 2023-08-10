# instance and class/static variable

# instance variable

'''
from tkinter import Variable


class Sample:
    def __init__(self):
        self.x = 10

    def modify(self):
        self.x += 1

s1 = Sample()
s2 = Sample()
print("x in s1 ",s1.x)
print("x in s2 ",s2.x)

s1.modify()
print("After modify :")
print("x in s1 ",s1.x)
print("x in s2 ",s2.x)

'''
# class/static Variable

class Sample2:
    x = 10

    @classmethod
    def modify(self):
        self.x += 1
    
s1 = Sample2()
s2 = Sample2()
print("x in s1 ",s1.x)
print("x in s2 ",s2.x)

s1.modify()
print("x in s1 ",s1.x)
print("x in s2 ",s2.x)
