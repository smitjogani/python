# Ways to remove i’th character from string

# naive method

test_str = "SmitJogani"

print("The original string is : " +test_str)

new_str = ""

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("The string after removal of i'th character :" + new_str)