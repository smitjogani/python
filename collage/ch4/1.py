# handle some built in exception like ZeroDivision Error.

try:
	x = int(input("Enter no1 :"))
	y = int(input("Enter no2 :"))
	
	z = x/y

	print("Division of two numbers is %d"%z)

except ZeroDivisionError:
	print("You can't divide value with %d"%y)