# 2-2. Create a program to retrieve, display and update only a range of elements from an array using indexing and slicing in arrays.
from array import array as arr

my_arr = arr('i',[33, 7, -13, 45, 90])

print(my_arr)
# displaying elements using indexing and slicing
print(my_arr[2])
print(my_arr[3:])
# updating elements using indexing and slicing
my_arr[0] = 123
print(my_arr)
my_arr[2:4] = arr(my_arr.typecode, [50, -86, 2])
print(my_arr)
