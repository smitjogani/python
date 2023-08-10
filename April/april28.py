# Average using constructer

class Students:

    def __init__(self,name,maths,english,gujarati):
        self.avg = (maths + english + gujarati) / 3
        self.name = name

    def print_data(self):
        return f"The Average of {self.name} is {self.avg}"

smit = Students("smit", 50, 50, 50)
mit = Students("mit", 19, 16, 18)

print(smit.print_data())
print(mit.print_data())
