# 2-16. Create a sample list of 7 elements and implement the list methods mentioned: append, insert, copy, extend, count, remove, pop, sort, reverse and clear.
lst = [1, 2, 3, 4, 5, 6, 7]
print("Original list:", lst)

# append
lst.append(8)
print("List after appeding 8:", lst)

# insert
lst.insert(2, 8)
print("List after inserting 8 at index 2:", lst)

# copy
copy_lst = lst.copy()
print("Copy of list:", lst)

# extend
lst.extend(copy_lst)
print("List after extending it with a copy of itself:", lst)

# count
print("Number of times 8 occurs in the list:", lst.count(8))

# remove
lst.remove(8)
print("List after removing 8:", lst)

# pop
print("Element popped from the list:", lst.pop())
print("List after using pop:", lst)

# sort
lst.sort()
print("List after sorting:", lst)

# reverse
lst.reverse()
print("List after reversing:", lst)

# clear
lst.clear()
print("List after clearing all elements:", lst)
