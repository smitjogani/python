# 8. Write a python program to find the sum of even numbers using command line arguments.
from sys import argv
print("Sum of even numbers", sum([int(num) for num in argv[1:] if int(num) % 2 == 0]))
