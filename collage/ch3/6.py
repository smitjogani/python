# create a static method that counts the number of instance created for a class

class MyClass:
    n = 0

    def __init__(self):
        MyClass.n += 1
    
    @staticmethod
    def noOfObjects():
        print("No. of instance created : ", MyClass.n)

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
MyClass.noOfObjects()