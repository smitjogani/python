'''
Health Management System

3-client :  smit,mit,sumit

total 6 files:
write a function when executed takes as input client name

'''

import datetime

def gettime():
    return datetime.datetime().now()

choice = int(input("Enter 1 for Lock & 2 for retrive"))

info = int(input("1 for Exercise Information & 2 for Food Information"))

client_name = int(input("1 for Smit & 2 Harsh & 3 for Jay"))

# Smit

if choice == 1 and info == 1 and client_name == 1:
    with open("health manage ment\smit-exercise.txt" , "a") as se:
        no_items_exe = int(input("no. of items :"))

        for item in range(0,no_items_exe):
            print(f"Write an item {item + 1} :")
            items_add = input("")
            se.write(items_add + "\n")
        print("succesfully written........")

if choice == 2 and info == 2 and client_name == 1:
    with open("health manage ment\smit-exercise.txt") as f:
        a = f.read()
        print(a)

if choice == 1 and info == 2 and client_name == 1:
    with open("health manage ment\smit-food.txt" , "a") as sf:
        no_items_food = int(input("Enter the  number of items :"))

        for item in range(0,no_items_food):
            print(f"Write an item {item + 1} :")
            items_add_food = input("")
            sf.write(items_add_food + "\n")
        print('successfully written.......')

if choice == 2 and info == 2 and client_name == 1:
    with open('health manage ment\smit-food.txt') as d:
       a = d.read()
       print(a)

# harsh

if choice == 1 and info == 1 and client_name == 2:
    with open("health manage ment\harsh-exercise.txt" , "a") as he:
        no_items_exe = int(input("no. of items :"))

        for item in range(0,no_items_exe):
            print(f"Write an item {item + 1} :")
            items_add = input("")
            he.write(items_add + "\n")
        print("succesfully written........")

if choice == 2 and info == 1 and client_name == 2:
    with open("health manage ment\harsh-exercise.txt") as f:
       a = f.read()
       print(a)

if choice == 1 and info == 2 and client_name == 2:
    with open("health manage ment\harsh-food.txt" , "a") as hf:
        no_items_food = int(input("Enter the  number of items :"))

        for item in range(0,no_items_food):
            print(f"Write an item {item + 1} :")
            items_add_food = input("")
            hf.write(items_add_food + "\n")
        print('successfully written.......')

if choice == 2 and info == 2 and client_name == 2:
    with open('health manage ment\harsh-food.txt') as d:
       a = d.read()
       print(a)

# raj

if choice == 1 and info == 1 and client_name == 3:
    with open("health manage ment\jay-exercise.txt" , "a") as re:
        no_items_exe = int(input("no. of items :"))

        for item in range(0,no_items_exe):
            print(f"Write an item {item + 1} :")
            items_add = input("")
            re.write(items_add + "\n")
        print("succesfully written........")

if choice == 2 and info == 1 and client_name == 3:
    with open("health manage ment\jay-exercise.txt") as f:
      a = f.read()
      print(a)

if choice == 1 and info == 2 and client_name == 3:
    with open("health manage ment\jay-food.txt" , "a") as rf:
        no_items_food = int(input("Enter the  number of items :"))

        for item in range(0,no_items_food):
            print(f"Write an item {item + 1} :")
            items_add_food = input("")
            rf.write(items_add_food + "\n")
        print('successfully written.......')

if choice == 2 and info == 2 and client_name == 3:
    with open('health manage ment\jay-food.txt') as d:
       a = d.read()
       print(a)
