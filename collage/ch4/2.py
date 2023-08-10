from logging import exception


# handle multiple exceptions like SyntaxError and TypeError

try:
    ex = eval(input("Enter Expression :"))
    print("Expression : ", ex)
    a = [1,2,3,4,5]
    b = []

    c = a/b
    print(c)

except (TypeError, SyntaxError):
    print("Syntax Error or Type Error")
    