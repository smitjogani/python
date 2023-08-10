# tack the size of the list from user

size = int(input("Enter the size of list :"))

# empty list
myList = []

# take input elements of the list from user
i = 1
for i in range(size):
    myList.append(int(input("Enter the element of list :")))

# Display the list
print(f"Your list is {myList} \n")

# first method of reverse the list
reverse1 = myList[:]
reverse1.reverse()
print(f"My first reverse list of {myList} is {reverse1}")

# reverse the list using slicing
print(f"My secondreverse list of {myList} is {myList[::-1]}")

# reverse the list using
reverse3 = myList[:]
for i in range(len(myList)):
    myList[i], myList[len(myList) - i -
                      1] = myList[len(myList) - i - 1], myList[i]

print(f"My third reverse list of {myList} is {reverse1}")