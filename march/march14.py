# Find the largest element is in array

def largest(arr,i):
    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10,324,38,478,903]

n = len(arr)

ans = largest(arr, n)
print("Largest element in given array is ", ans)