# 9. Write a menu driven python program which perform the following:
# Find area of circle
# Find area of triangle
# Find area of square and rectangle
# Find Simple Interest
def circle_area():
    print("Area of the Circle:", 3.14 * int(input("Enter Radius: ")) ** 2)

def triangle_area():
    print("Area of the Triangle:", int(input("Enter Base: ")) * int(input("Enter Height: ")) * 0.5)

def rect_area():
    print("Area of the Square/Rectangle:", int(input("Enter Length: ")) * int(input("Enter Width: ")))

def simple_interest():
    print("Simple Interest:", int(input("Enter Principal Amount: ")) * float(input("Enter Rate of Interest: ")) * int(input("Enter Number of Years: ")) * 0.01)

choice = 0
while True:
    print("\n\t\tMenu\t\t\n1. Find Area of a Circle\n2. Find Area of a Triangle\n3. Find Area of a Square/Rectangle\n4. Find Simple Interest\n5. Exit\n")
    choice = int(input("Enter choice: "))
    menu = {1: circle_area, 2: triangle_area, 3: rect_area, 4: simple_interest, 5: exit}
    menu.get(choice,"Invalid choice")()
