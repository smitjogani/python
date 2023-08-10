# cube sum of first n nutural number

def sum_of_series(n):
    x = (n * (n + 1) / 2)
    return (int)(x * x)

n = int(input("Enter the value of n:"))
print(sum_of_series(n))