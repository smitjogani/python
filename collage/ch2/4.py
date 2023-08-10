# 2-4. Write a program to sort the array elements using bubble sort technique.
from array import array as arr

my_arr = arr('i',[12, 42, 18, 5, 10, 39, -28, 31])
n = len(my_arr)

for i in range(n):
    for j in range(n-1):
        if my_arr[j] > my_arr[j+1]: my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]

print(my_arr)
