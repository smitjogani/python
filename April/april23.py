# pattern printing 

'''

input = integert number

boolean = True or False

True :
*
* *
* * * 
* * * *

False:

* * * *
* * *
* *
*

'''
input_number = int(input("Enter the number 0 or 1:"))

n = int(input("Enter the number of rows :"))

if input_number == 1:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end = " ")
        print()
elif input_number == 0:
    for i in range(n + 1,0,-1):
        for j in range(0,i-1):
            print("*", end = " ")
        print("")
else:
    print("Enter valid number 0 or 1")