# check if a string is palindrome or not

def isPalindrome(s):
    return s == s[::-1]

s = input("Enter the String:")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("NO")

