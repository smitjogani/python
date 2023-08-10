# factorial number

def Factorial(n):
        if (n == 1or n == 0): 
            return 1 
        else:
             return n * Factorial(n - 1)
num = int(input("Enter the value of number :"))
print("Factorial of is ")
print(Factorial(num))