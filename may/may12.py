# print the next palindrome

# define the function which give next_palindrome

def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n = n + 1
    return n

# ths function is tell the number is palindrom or not
def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':

    # take input
    n = int(input("Enter the number which you like to test :"))

    # empty list
    number = []

    for i in range(n):
        num = int(input("Enter the number :   "))
        #append number in list
        number.append(num)

    for i in range(n):
        print(
            f"The next palindrome {number[i]} is {next_palindrome(number[i])}")