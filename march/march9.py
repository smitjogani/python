# make a simple calculater

def add(p,q):
    # used for addition of two numbers
    return p + q

def sub(p,q):
    # used for subtraction of two numbers
    return p - q


def mul(p,q):
    # used for multiplying of two numbers
    return p*q

def divide(p,q):
    # used for division of twonumbers
    return p / q

print("Selecrt the options:")

print("A.Addition")
print("B.Subtraction")
print("C.Multipliction")
print("D.Division")

choice = input("Enter Your choice :")

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

if(choice == 'A' or choice == 'a'):
    print("The sum of ",num1," and ",num2," is :" ,add(num1, num2))

elif(choice == 'B' or choice == 'b'):
    print("The subttraction of ",num1," and ",num2," is :" ,sub(num1, num2))

elif(choice == 'C' or choice=='c'):
    print("The multiplication of ",num1," and ",num2," is :" ,mul(num1, num2))

elif(choice == 'D' or choice == 'd'):
    print("The division of ",num1," and ",num2," is :" ,divide(num1, num2))

else:
    print("Enter valid number......")