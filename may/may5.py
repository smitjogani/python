# Write a function to print the sum of all odd numbers from 1 to n

def print_sum(n):
    sum = 0
    
    for i in range(1,n):
        if i % 2 == 0:
            sum = sum + 1
            
    print(f"The sum of {n} odd numer is {sum}")
    
n = int(input("Enter the value of n :"))

print_sum(n)