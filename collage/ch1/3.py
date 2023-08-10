# 3. Write a program to create a bytearray type array, read, modify, and display the elements of the array
def display():
    print(list(byte_array))

def modify():
    i = int(input("Enter index to modify: "))
    byte_array[i] = int(input("Enter new value: "))

def append():
    byte_array.append(int(input("Enter new element: ")))

def insert():
    byte_array.insert(int(input("Enter index to insert at: ")),int(input("Enter new element: ")))

def delete():
    del byte_array[int(input("Enter index to delete: "))]

def invalid():
    print("Invalid choice")

temp_lst = [int(ele) for ele in input("Enter elements of array (separate elements with spaces): ").split() if int(ele)>-1 and int(ele)<256]
byte_array = bytearray(temp_lst)
print("Created array: ", list(byte_array))
choice = 0
while True:
    print("\n\tMenu\t\n1. Display array\n2. Modify elements\n3. Append elements\n4. Insert elements\n5. Delete elements\n6. Exit\n")
    choice = int(input("Enter choice: "))
    menu = {1: display, 2: modify, 3: append, 4: insert, 5: delete, 6: exit}
    menu.get(choice,invalid)() # gives error when choice is invalid
