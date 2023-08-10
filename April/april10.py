# Python Program to Display Fibonacci Sequence Using Recursion

def rec_fibo(n):
    if n <= 1:
        return n
    else:
        return (rec_fibo(n - 1) + rec_fibo(n - 2))

num = int(input("Enter the number :"))

if num <= 0:
    print("Enter positive number...!")
else:
    print("Fibonacci Series ")
    for i in range(num):
        print(rec_fibo(i))
