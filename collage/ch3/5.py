# use class method to handle the common features of all the instance of student class

class Student:
    semester = 5

    @classmethod
    def study(self,sem):
        print(f"{sem} is studies in semester {self.semester}")

Student.study("smit")
Student.study("mit")