# 2-13. Create a program name “employee.py” and implement the functions DA, HRA, PF, and ITAX. Create another program that uses the function of employee module and calculates gross and net salaries of an employee.
from employee import *

basic = float(input("Enter basic salary:"))
gross = basic + da(basic) + hra(basic)
net = gross - pf(basic) - itax(gross)

print("Gross Salary: %.2f\nNet Salary: %.2f" % (gross, net))
