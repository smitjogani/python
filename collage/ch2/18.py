# 2-18. Write a program to accept elements in the form of a tuple and display its minimum, maximum, sum and average.
tpl = eval(input("Enter tuple: "))
print("Minimum: {}\nMaximum: {}\nSum: {}\nAverage: {}".format(min(tpl), max(tpl), sum(tpl), sum(tpl)/len(tpl)))
