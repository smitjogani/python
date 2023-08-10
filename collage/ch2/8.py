# 2-8. Write a program to pass a list to a function and display it.
def display_list(lst):
    print(*lst)

lst = eval(input("Enter a list: "))
display_list(lst)
