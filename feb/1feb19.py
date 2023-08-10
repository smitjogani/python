# Python program to interchange first and last elements in a list

num = [12,23,45,67,89,34]

def swaplist(num):
    # Find length
    size = len(num)

    # Swapping
    temp = num[0]
    num[0] = num[size- 1]
    num[size - 1] = temp

    return num

print(swaplist(num))