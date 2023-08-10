# 2-7. Write a python program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
lst = eval(input("Enter a list:"))
new_lst = []
for ele in lst:
    if ele not in new_lst: new_lst.append(ele)

print("New list:", new_lst)
