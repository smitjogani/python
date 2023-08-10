# convert number decimal to binary and octal to hexadecimal

# function which convert decimal to binary
def decimal_into_binaary(decimal_1):
    decimal = int(decimal_1)

    # print the equvalent decimal
    print("The given decimal number ",decimal," in binary number is :",bin(decimal))

# function which convert decimal to octal
def decimal_into_octal(decimal_1):
    decimal = int(decimal_1)

    # print to equvalent octal
    print("The given decimal number ",decimal," in octal number is:",oct(decimal))

# function which convert decimal to hexadecimal
def decimal_into_hexadecimal(decimal_1):
    decimal = int(decimal_1)

    # print the hexadecimal number
    print("The given decimal number ",decimal," in hexadecimal number is :" ,hex(decimal))

decimal_1 = int(input("Enter the decimal number :"))

decimal_into_binaary(decimal_1)
decimal_into_hexadecimal(decimal_1)
decimal_into_octal(decimal_1)