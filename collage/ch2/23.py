# 2-23. Create a python function to accept a dictionary and display its elements.
dict = {'A': 'Apple', 'B': 'Ball', 'C': 'Car'}

def display(dict):
    print("Key\t\tValue")
    for key, val in dict.items(): print("{}\t\t{}".format(key, val))

display(dict)
