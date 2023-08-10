# 2-14. Write a program to create a list using range functions and  perform  append,  update  and  delete  elements operations in it.
start, end, jump = int(input("Enter starting value: ")), int(input("Enter ending value: ")) + 1, int(input("Enter step size: "))
lst = list(range(start, end, jump))
print("Created list: ", lst)

# Appending an element
val = int(input("Appending an element:\nEnter value to append: "))
lst.append(val)
print("List after appeding {}: {}".format(val, lst))

# Updating elements
start, end = int(input("Updating elements:\nEnter starting index of elements to update: ")), int(input("Enter ending index of elements to update (enter same ending index as starting index if you only want to update one element): ")) + 1
for i in range(start, end):
    lst[i] = int(input("Enter value to replace {} with at index {}: ".format(lst[i], i)))
print("List after updating elements:", lst)

# Deleting an element
del lst[int(input("Deleting an element:\nEnter index of element you want to delete: "))]
print("List after deleting elements:", lst)
