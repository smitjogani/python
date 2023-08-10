# 2-10. Write a program to show variable length argument and its use.
def var_len_args(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("""var_len_args [0 arguments]:
    Arguments:
    Return value: """, var_len_args())
print("""var_len_args [1 arguments]:
    Arguments: {}
    Return value: {}""".format(1, var_len_args(1)))
print("""var_len_args [2 arguments]:
    Arguments: {}, {}
    Return value: {}""".format(1, 2, var_len_args(1, 2)))
print("""var_len_args [3 arguments]:
    Arguments: {}, {}, {}
    Return value: {}""".format(1, 2, 3, var_len_args(1, 2, 3)))
