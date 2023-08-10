# create a bank class with two variables name and balance.implement a constructer to initilize the variables. impliment deposite and withdrawls using instence method

import sys

class Bank:
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Balanace amount is low!!!!!")
        else:
            self.balance -= amount
        return self.balance

name = input("Enter Name : ")
b = Bank(name)

while(True):
    print("d - Deposite  w - Withdraw  e-Exit")

    choice = input("Enter d or w or e :")

    if choice == 'e' or choice == 'E':
        sys.exit()
    
    amt = float(input("Enter amount :"))    

    if choice == 'd' or choice == 'D':
        print("Balance after deposite : ", b.deposite(amt))

    elif choice == 'w' or choice == 'W':
        print("Balance after withdrawal : ", b.withdraw(amt))

