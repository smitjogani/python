# check whether the string is Symmetrical or Palindrome

string = input("Enter the String :")
half = int(len(string) / 2)

if len(string) % 2 == 0:
    first_str = string[:half]
    second_str = string[half:]

else:
    first_str = string[:half]
    second_str = string[half + 1]

if first_str == second_str:
    print('string is symmertical')
else:
    print('String is not symmertical')

if first_str == second_str[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
    

