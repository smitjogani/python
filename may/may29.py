# Python Program to Count the Number of Occurrence of a Character in String

# Using for loop

count = 0

my_str = input("Enter the string  :")
my_char = input("Enter the character which one you like to find :")

for i in my_str:
    if i == my_char:
        count += 1
        
print(f" '{my_char}' is repeted {count} time in ' {my_str} '")

# using modual

print(my_str.count(my_char))