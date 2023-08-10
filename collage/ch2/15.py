# 2-15. Write a program to combine two list, perform repetition of lists and create cloning of lists.
lst1, lst2 = eval(input("Enter list one: ")),eval(input("Enter list two: "))
print("Original lists:\n\t", lst1, "\n\t", lst2)

# combining lists
print("Combined list:", lst1 + lst2)

# repeating list
print("Repeating list one 3 times:", lst1 * 3)

# cloning a list
clone_lst = lst1[:]
print("Clone of list one:", clone_lst)
clone_lst.append(8)
print("Clone of list one after appending 8:", clone_lst)
print("List one after appending 8 to clone of list one:", lst1)
