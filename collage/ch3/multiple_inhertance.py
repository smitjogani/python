class Family:
    def show_family(self):
        print("My Sweet Family🤗")

class Dad(Family):
    dadname = ""
    def show_dad(self):
        print(self.dadname)

class Mom(Family):
    momname = ""
    def show_mom(self):
        print(self.momname)

class Son(Dad,Mom):
    def show_parent(self):
        print("Son : It's me")
        print("Dad : ", self.dadname)
        print("Mom : ",self.momname)

s1 = Son()
s1.dadname = "Daddy"
s1.momname = "Mommy"
s1.show_family()
s1.show_parent()