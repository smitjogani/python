
# next_palindrome function which return the next palindrome number
def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

# is_palindrome function is check string or reverse strings are same or not


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':

    # taking the size of list from user
    size = int(input("Enter the size of your list : "))

    # blank list
    num_lst = []

    for i in range(size):

        # append the elements of the list which are taken from the user
        num_lst.append(int(input("Enter the number of the list : ")))

    # print the list with the entered elements
    print(f"INPUT : {num_lst}")

    # empty list for store the outputed list
    new_lst = []

    # for element in num_lst:
       #    first method
       # condition for printing next palindrome number
       if element >= 10:
            nxt = next_palindrome(element)
            new_lst.append(nxt)
        else:

            # it's append inputed number
            new_lst.append(element)

    # throw the output
    print(f"OUTPUT : {new_lst}")

    # second method
    print(f"OUTPUT LIST : {[num_lst[i] if num_lst[i] < 10 else next_palindrome(num_lst[i]) for i in range(size)]}")