# faulty calculater

print("-- OPTIONS --")

print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

print("Enter Your Choice :",end=" ")
choice = int(input())

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))

if choice == 1:
    print(f"Addition of {n1} and {n2} is {n1 + n2}")    
elif choice == 2:
    print(f"Subttraction of {n1} and {n2} is {n1 - n2}")    
elif choice == 3:
    print(f"Multiplication of {n1} and {n2} is {n1 * n2}")    
elif choice == 4:
    print(f"Division of {n1} and {n2} is {n1 / n2}")    
else:
    print("ERROR!!......")