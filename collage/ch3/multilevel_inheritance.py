class Student:
    def getStudent(self):
        self.name = input("Enter The Name : ")
        self.gender = input("Enter The Gender : ")

class Exam(Student):
    def getMarks(self):
        print("Enter the marks of the respective subject : ")
        self.cn = int(input("Computer Network : "))
        self.pp = int(input("Python Programming : "))
        self.wap = int(input("Web Application devlopment : "))
        self.mad = int(input("Mobile Application Devlpment : "))
    
class Marks(Exam):
    def dispaly(self):

        self.sum = self.cn + self.pp + self.waps + self.mad

        print("Name        : ",self.name)
        print("Gender      : ",self.gender)
        print("Total Marks : ",self.sum)

m1 = Marks()
m1.getStudent()
m1.getMarks()
m1.dispaly()