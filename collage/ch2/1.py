# 2-1. Write a program to create one array from another array.
from array import array as arr

arr1 = arr('i',[-2, 0, 6])
arr2 = arr(arr1.typecode, (ele for ele in arr1))

print(arr1)
print(arr2)
