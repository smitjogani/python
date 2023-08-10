# check out the errors and give soluction of errors

import random

# rohanMultiplication function which was print wrong table


def rohanMultiplication(number):

    # random number generate between 0 to 9
    wrong = random.randint(0, 9)

    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 9)

    return table

# is_correct function which print true table


def is_correct(table, numer):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i - 1
    return None


if __name__ == '__main__':
    
    # get input number fromm user
    number = int(input("Enter a number : "))
    
    myTable = rohanMultiplication(number)
    
    print(myTable)

    # define wrong table index
    wrongIndex = is_correct(myTable, number)

    print(f"The table was wrong at index {wrongIndex}")
