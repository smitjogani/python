# Python Program to Find Sum of Natural Numbers Using Recursion

# Function
def rec_sum(n):
    if n <= 1:
        return n
    else:
        return n + rec_sum(n - 1)

# change the value of differeent results

num = int(input("Enter the number : "))

if num < 0:
     print("Enter the positive number...!")
else:
    print("the sum is ",rec_sum(num))