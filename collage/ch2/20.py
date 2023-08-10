# 2-20. Write a program to create a dictionary from the user and display the elements.
dict = {}
n = int(input("Enter number of elements: "))

for i in range(n):
    print("\nElement", i+1)
    key = input("Enter key: ")
    dict[key] = input("Enter value: ")

print("\nKey\t\tValue")
for key, val in dict.items():
    print("{}\t\t{}".format(key, val))
