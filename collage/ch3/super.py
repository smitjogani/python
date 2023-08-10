# to access parent class method/constructor in child class using super()

class Square:
    def __init__(self,length):
        self.length = length
    def area(self):
        print("Area Of Square is ",self.length * self.length)

class Rectangle(Square):
    def __init__(self,length,width):
        super().__init__(length)
        self.width = width

    def area(self):
        super().area()
        print("Area of Rectangle is ",self.length * self.width)
    
l = float(input("Enter the Length :"))
b = float(input("Enter the Width :"))
r = Rectangle(l,b)
r.area()