# Check if element exists in list 

test_list = [1,2,3,4,5,6]

print("Checking if 4 is exists in list :")

# Using loop
for i in test_list:
    if(i == 4):
        print("Element is exists")
    else:
        print("Element is not exists")

# using in

if(4 in test_list):
    print("Element is exists")
else:
    print("Element is not exists")