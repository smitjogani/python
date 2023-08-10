# to check prime number or not

num = int(input("enter the number :"))

flag = False;

if num > 1:
    for i in range(2,num):
        if(num % i == 0):
            flag = True
            break

if flag==True:
    print(num ,"is not a prime number")
else:
    print(num,"is prime number")


