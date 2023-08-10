# 2-5. Create a program to search the position of an element in an array using index() method of array class.
from array import array as arr

my_arr = arr('i',[12, 42, 18, 5, 10, 39, -28, 31])

print(my_arr)
val = int(input("Enter value to search for: "))
print("Index of", val, "is", my_arr.index(val))
