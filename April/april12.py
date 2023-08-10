# Python Program to Find Factorial of Number Using Recursion

# function

def rec_sum_factorial(n):
    if n == 1:
        return n
    else:
        return n * rec_sum_factorial(n - 1)

# check if number is negative

num = int(input("Enter the number :"))

if num < 0:
    print("Enter positive numbers.....")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial os " , num ," is ", rec_sum_factorial(num))