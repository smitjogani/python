# guess the age in 2090

age = int(input("Enter Your Age :"))
birth_year = int(input("Enter Your Birth Year :"))

if age < 1900:
    print("You are oldest person who is alive")
    
if birth_year > 2022:
    print("You are not born yet")
else:
    print("You are die")
    
y = 2090 - birth_year
req = 100 - age
year = birth_year + 100

print(f"Your Age in 2090 will {y}")

if y <= 100 :
    print(f"In next {req} year you will be turn 100 years old in {year}")
else:
    pass