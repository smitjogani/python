# sum of squares of n nutural numbers

def sqrsum (n):
    sum = 0
    for i in range(1,n + 1):
        sum = sum + (i * i)
    return sum

n = int(input("Entert the value of n is "))

print(sqrsum(n))

