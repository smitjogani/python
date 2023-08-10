#  Enter three numbers from the user & make function to print their average

def average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    print(f"The average of {num1} {num2} {num3} is {avg}")
    return avg

n1 = int(input("Enter the number 1 :"))
n2 = int(input("Enter the number 2 :"))
n3 = int(input("Enter the number 3 :"))

average(n1, n2, n3)