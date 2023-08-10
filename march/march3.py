# Check the given number is fibonaki number or not

import math

def inPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return inPerfectSquare(5 * n * n + 4) or inPerfectSquare(5 * n * n - 4)

for i in range(1,11):
    if (isFibonacci(i) == True):
        print(i," is Fibonacci number")
    else:
        print(i," is not fibonacci number")