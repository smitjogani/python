# Sum of n nutural number 

n = int(input("Enter the number:"))
sum = 0
for i in range(0,n+1,1):
    sum = sum + i
print(f"Sum of {n} number is {sum}")