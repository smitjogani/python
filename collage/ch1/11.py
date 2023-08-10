# 11. Write a program to search an element in the list using for loop and also demonstrate the use of “else” with for loop.
lst = input("Enter elements of list (separate elements with spaces): ").split()
search_ele = input("Enter element to search: ")
for ele in lst:
    if ele == search_ele:
        print(search_ele,"is in the list")
        break
else:
    print(search_ele,"is not in the list")
