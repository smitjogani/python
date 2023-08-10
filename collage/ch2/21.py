# 2-21. Create a dictionary that will accept cricket players name and scores in a match. Also we are retrieving runs by entering the player’s name.
crkt_dict = {}
n = int(input("Enter number of players: "))

for i in range(n):
    print("\nPlayer", i+1)
    key = input("Enter player's name: ")
    crkt_dict[key] = input("Enter runs: ")

print("\nPlayer Names:", ", ".join(crkt_dict.keys()))
name = input("Enter name of a player: ")
print("{}'s runs: {}".format(name,crkt_dict.get(name,"Unknown")))
