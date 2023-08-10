# Write a function that takes in the radius as input and returns the circumference of a circle

def circumference(radius):
    c =  2 * 3.14 * radius
    print(f"The circumference of circle is {c}")
    return c

rad = int(input("Enter the value of radius : "))

circumference(rad)    