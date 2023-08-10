# Write a function which takes in 2 numbers and returns the greater of those two.

def max(n1, n2):
    if n1 > n2:
        print(f"{n1} is greater than {n2}")
    elif n1 == n2:
        print(f"{n1} and {n2} both equal values")
    else:
        print(f"{n2} is greater than {n1}")


num1 = int(input("Enter the value of number 1 :"))
num2 = int(input("Enter the value of number 2 :"))

max(num1, num2)
