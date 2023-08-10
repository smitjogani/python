# import random modual
import random


def guess_game(a, b, actual):
    guess = int(input(f"Guess the number between {a} and {b} \n:"))
    nguess = 1

    while guess != actual:
        if guess < actual:
            guess = int(input("Enter a bigger number .."))
            nguess += 1
        else:
            guess = int(input("Enter a smaller number .."))
            nguess += 1

    print(f"You gussed number in  {nguess} guesses \n")
    return nguess


if __name__ == '__main__':

    # taking the value of a and b from user
    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))

    actual1 = random.randint(a, b)

    print("Player 1's turn....")
    g1 = guess_game(a, b, actual1)

    print("Player 2's turn....")
    actual2 = random.randint(a, b)
    g2 = guess_game(a, b, actual2)

    if g1 < g2:
        print("player 1 won the match...:) ")

    elif g1 > g2:
        print("player 2 won the match...:) ")

    else:
        print("It's a draw")

    # print the attemp of guessing number
    print(
        f"The number for player 1 is {actual1} and for player 2 is {actual2}")
