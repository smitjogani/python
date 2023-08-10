# 5. Write a program to find out and display the common and the non common elements in the list using membership operators
lst1, lst2 = input("Enter elements of list 1 (separate elements with spaces): ").split(), input("Enter elements of list 2 (separate elements with spaces): ").split()

# Method 1 - using membership operators
print("Common elements: ", [ele for ele in lst1 if ele in lst2])
print("Uncommon elements: ", [ele for ele in lst1 if ele not in lst2]+[ele for ele in lst2 if ele not in lst1])

# Method 2 - using set operators
set1, set2 = set(lst1), set(lst2)
print("Common elements: ", set1.intersection(set2))
print("Uncommon elements: ", (set1.difference(set2)).union(set2.difference(set1)))
