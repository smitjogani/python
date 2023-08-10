#elif  leader

age = int(input("Enter your age :"))

if age > 18:
    print("You are eligible for drive")
elif age < 18:
    print("You are not eligible for drive")
else:
    print("We can't decide")