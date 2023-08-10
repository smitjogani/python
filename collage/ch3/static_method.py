from math import factorial


class Factorial:
    @staticmethod
    def fact(num):
        if num == 0:
            return 1
        else:
            return num * Factorial.fact(num - 1)

n = int(input("Enter the number : "))
factorial = Factorial.fact(n)
print(f"Factorial of {n} is {factorial}")