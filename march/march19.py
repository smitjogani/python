# Python Program for Find remainder of array multiplication divided by n

def findReminder(arr,len,n):
    mul = 1

    # Find the individual reminder
    for i in range(len):
        mul = (mul * (arr[i] % n)) % n
    return mul % n

# Driven code
arr = [100,10,5,25,35,14]
len = len(arr)
n = int(input("Enter the value of n :"))
print(findReminder(arr, len, n))
