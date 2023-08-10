# implement multiple inheritance using two base classes

class Father:
    def height(self):
        print("Height is 6.0 feet")
    
class Mother:
    def color(self):
        print("Color is Brown")
    
class Child(Father, Mother):
    pass

c = Child()
print("Child's inherited quilities : ")
c.height()
c.color()