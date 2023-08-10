# 2. Write a program to display sum of two complex numbers.
print("Enter 2 complex numbers (separate real and imaginary parts with spaces):")
compNo1, compNo2 = [complex(float(real), float(imaginary)) for real, imaginary in (input("\tEnter 1st complex number: ").split(), input("\tEnter 2nd complex number: ").split())]
print(compNo1, "+", compNo2, "=", compNo1+compNo2)

# print("Enter complex number 1: ")
# real = float(input("Enter real part: "))
# imag = float(input("Enter imaginary part: "))
# comp_no1 = complex(real, imag)
#
# print("Enter complex number 2: ")
# real = float(input("Enter real part: "))
# imag = float(input("Enter imaginary part: "))
# comp_no2 = complex(real, imag)
#
# print("Sum is", comp_no1+comp_no2)
