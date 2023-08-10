# 1. Write a program to swap two numbers without taking a temporary variable.
num1, num2 = int(input("Enter number 1: ")), int(input("Enter number 2: "))
print("Initial values\n\tnumber 1: {}\n\tnumber 2: {}".format(num1, num2))
num1, num2 = num2, num1
print("Swapped values\n\tnumber 1: {}\n\tnumber 2: {}".format(num1, num2))
