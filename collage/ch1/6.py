# 6. Create a program to display memory locations of two variables using id() function, and then use identity operators two compare whether two objects are same or not.
var1, var2 = input("Enter variable 1: "), input("Enter variable 2: ")
print("id of variable 1:", id(var1), "\nid of variable 2:", id(var2))
print("objects are same" if var1 is var2 else "objects are different")
