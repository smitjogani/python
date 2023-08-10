# number guessing game

win_num =  34

input_num = int(input("Guess the number between 1 to 100 :"))

game_over = False
guess = 1

while not game_over:
    if(win_num == input_num):
        print(f"You win and you can guess it in {guess} time")
        game_over = True
    else:
        if input_num > win_num:
            print("it is high number")
            guess += 1
            input_num = int(input("Guess again .."))
        else:
            print("it is low number")
            guess += 1
            input_num = int(input("Guess again .."))