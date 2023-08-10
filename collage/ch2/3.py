# 2-3. Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.
from array import array as arr

my_arr = arr('i',[6, 5, 4, 3, 2, 1])

print("Initial array:", my_arr)
# append
my_arr.append(9)
print("Array after appending 9:", my_arr)
# insert
my_arr.insert(0, 7)
print("Array after inserting 7 at position 0:", my_arr)
# remove
my_arr.remove(9)
print("Array after removing 9:", my_arr)
# pop
a = my_arr.pop()
print("Array after using pop:", my_arr)
print("Popped element:", a)
# index
print("Position of 4 in the array is:", my_arr.index(4))
# tolist
print("Array converted to a list:", my_arr.tolist())
# count
print("Number of times 3 occurs in the array:", my_arr.count(3))
