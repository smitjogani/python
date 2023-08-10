# store data into instance using mutator methods and to retrive data from instance using accessor method

class Student:
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = int(input("How many student? : "))

i = 0
while(i < n):
    s1 = Student()

    name = input("Enter Name : ")
    s1.setName(name)
    s1.getName()

    marks = int(input("Enter marks : "))
    s1.setMarks(marks)
    s1.getMarks()

    i += 1
    print("--------------------\n")