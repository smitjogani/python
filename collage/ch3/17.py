# using method overloading find the sum of two and three numbers

class MyClass:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("sum is ", a+b+c)
        elif a != None and b != None:
            print("Sum is ", a+b)
        else:
            print("Please enter two or three arguments")

m = MyClass()
m.sum(1,2,3)
m.sum(10.5,20.5)
m.sum(12)