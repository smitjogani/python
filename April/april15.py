# Python program to find H.C.F of two numbers

def com_hcf(x,y):

    # choose the smaller number
    if x > y :
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))

print("the H.C.F is ", com_hcf(num1, num2))