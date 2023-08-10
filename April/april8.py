# Python Program to Find Armstrong Number in an Interval

lwr = int(input("Enter the lowest number:"))
upr = int(input("enter highes number:"))

for num in range(lwr,upr + 1):
    # order of number
    odr = len(str(num))

    # intilize sum

    sum = 0

    tem = num

    while tem > 0:
        digit = tem % 10

        sum += digit ** odr

        tem //= 10

    if num == sum:
        print("The armstrong numbers are :" ,num)