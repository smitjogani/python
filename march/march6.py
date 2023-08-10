# Python programm to find H.C.M. of two numbers using two numbers

def calculate_hcm(x , y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller +1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

print("The H.C.M. of ",num1," and ",num2," is ",calculate_hcm(num1, num2))