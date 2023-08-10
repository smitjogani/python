def multiply(mylist):
    result = 1

    for x in mylist:
        result = result * x
    return result

list1 = [1,2,3]
list2 = [3,2,4]

print(multiply(list1))
print(multiply(list2))