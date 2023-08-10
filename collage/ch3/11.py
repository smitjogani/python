# override super class constructor and method in subclass

class Square:
    def __init__(self, x):
        self.x = x
    def area(self):
        print("Area of square : ", self.x * self.x)

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    
    def area(self):
        super().area()
        print("Area of Retangle ", self.x * self.y)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

e = Rectangle(a,b)
e.area()