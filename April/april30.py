# Parameterized constructor

class Fruits:
    total = 0

    def __init__(self,fno,fname,fcolor): #Constructer declaring using arguments
        self.fno = fno
        self.fname =fname
        self.fcolor = fcolor
        Fruits.total += 1

    def display_total(self):
        print(f"No : {self.fno} Name : {self.fname} Color : {self.fcolor}")

    def display_fruits(self):
        print(f"No : {self.fno} Name : {self.fname} Color : {self.fcolor}")
    
f1 = Fruits(1, "Apple", "Red")
f2 = Fruits(2, "Mango", "Oreange")

f1.display_fruits()
f2.display_fruits()

print(f"Total number of fruits are {Fruits.total}")