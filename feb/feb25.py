# print all prime number in interval

def prime(x,y):
    prime_list = []
    for i in range(x,y):
        if i==0 or i==1:
            break
        else:
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
                else:
                    prime_list.append(i)
    return prime_list

starting_range = 2
ending_range = 10
lst = prime(starting_range, ending_range)

if len(lst) == 0:
    print("There are no prime number")
else:
    print("There are prime number",lst)