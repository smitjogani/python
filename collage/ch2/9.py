# 2-9. Write a program to demonstrate the use of positional argument, keyword argument and default arguments.
def pos_args(str1, str2):
    return str1 + str2

def keyword_args(fname, lname):
    return fname + lname

def def_args(base, exp=2):
    return base**exp

print("""pos_args:
    Arguments: {}, {}
    Return value: {}""".format("Hello", "World", pos_args("Hello", "World")))
print("""keyword_args:
    Arguments: fname={}, lname={}
    Return value: {}""".format("John", "Doe", keyword_args(fname="John", lname="Doe")))
print("""keyword_args:
    Arguments: lname={}, fname={}
    Return value: {}""".format("Doe", "John", keyword_args(lname="Doe", fname="John")))
print("""def_args:
    Arguments: {}, {}
    Return value: {}""".format(3, 4, def_args(3, 4)))
print("""def_args:
    Arguments: {}
    Return value: {}""".format(5, def_args(5)))
