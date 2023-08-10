# 2-12. Create a decorator function to increase the value of a function by 3.
# function that returns 10
def ten():
    return 10

# decorator function that takes any function and returns a modified version of that function
def decorator(fun):
    def plus_three():
        return fun()+3
    return plus_three

print("Result of original function:", ten())
ten_plus_three = decorator(ten)
print("Result of decorated function:", ten_plus_three())
