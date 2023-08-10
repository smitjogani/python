# 2-22. Write a program to convert the elements of two lists into key-value pairs of a dictionary.
key_lst = ['Roll No', 'Name', 'Age']
val_lst = [100, 'Luffy', 19]
dict = dict(zip(key_lst, val_lst))

print("\nKey\t\tValue")
for key, val in dict.items():
    print(key+"\t\t"+str(val))
