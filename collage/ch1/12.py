# 12. Write a python program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. (2.54 = 1 inch).
cm = float(input("Enter length in centimeters: "))
assert cm > -1, "negative length is invalid"
print("%d centimeters is %.3f inches" %(cm, cm / 2.54))
