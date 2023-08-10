import random   

turn = 10
no_of_chance = 1
computer_point = 0
player_point = 0

while no_of_chance < turn:
    list = ["stone", "paper", "sesore"]

    player_select = input("Enter one of them (stone , paper , sesore) :")

    computer_select = random.choice(list)

    print(f"player select {player_select}")
    print(f"computer select {computer_select}")

    if (player_select == "stone" and computer_select == "sesore") or (player_select == "paper" and computer_select == "stone") or (player_select == "sesore" and computer_select == "paper"):
        player_point = player_point + 1
        print("Player is win")
        print(f"computer point is {computer_point} and player point is {player_point}")
    
    elif((computer_select == "stone" and player_select == "sesore") or (computer_select == "paper" and player_select == "stone") or (computer_select == "sesore" and player_select == "paper")):
        computer_point = computer_point + 1    
        print("Computer is win")
        print(f"computer point is {computer_point} and player point is {player_point}")
    
    elif((computer_select == "stone" and player_select == "stone") or (computer_select == "paper" and player_select == "paper") or (computer_select == "sesore" and player_select == "sesore")):
        print("Draw")
        print("Both point is 0...")
    
    else:
        print("Invalid choice")
        turn = turn + 1
        print(f"{turn - no_of_chance} is left out")