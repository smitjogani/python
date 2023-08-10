# Python program to find smallest number in a list

# method 1
list1 = [10,20,30,40,50]

list1.sort()

print("Smallest Element is :", *list1[:1])

# method 2

list = [10,20,30,40,50]

print("smallest eleement is :" ,min(list))