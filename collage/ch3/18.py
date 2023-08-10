# override a superclass method in subclass

import math

class Square:
    def area(self, x):
        print("Square area = %.4f"%x,x)

class Circle:
    def area(self, x):
        print("Circle area = %.4f" % (math.pi * x * x))

a = Circle()
a.area(20)