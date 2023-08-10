# 2-6. Write a program to generate prime numbers with the help of a function to test prime or not.
def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0: return False
    return True

def generate_prime_nos(n):
    num = 1
    count = 0
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1
    print()

n = int(input("How many prime numbers do you want to generate? "))
generate_prime_nos(n)
