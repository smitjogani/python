# find the ASCII value of number
ch = input("Enter the Character:")

print("The  ASCII value of ",ch," is :",ord(ch))

# For multiple for string

print("Enter the string :" , end="")

string = input()

string_length = len(string)

for i in string:
    ASCII = ord(i)

    print(i,"\t",ASCII)