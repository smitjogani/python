# minimum of two numbers

def minimum(a,b):
    if a >= b:
        return b
    else:
        return a

n1 = int(input("Enter the number1 :"))
n2 = int(input("enter the number2 :"))

min = str(minimum(n1, n2))

print("The minimum number is " + min)