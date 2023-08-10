# devide the apple

n = int(input("Enter the number of the apples :"))

mn = int(input("What is minimum number in range :"))
mx = int(input("What is maximum number in range :"))

i = 1
for i in range(mn, mx+1):
    if n % mn == 0:
        print(f"{mn} is a deviser of the {n}")
    else:
        print(f"{mn} is not a deviser of the {n}")

    mn += 1

    if mn == mx+1:
        break
