# Mean,Median, and Mode using python

'''

Mean - The average value
Median - The mid point value
Mode - The most common value

'''

import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean of speed
x = numpy.mean(speed)

# Median of speed
y = numpy.median(speed)

# Mode of speed
from scipy import stats
z = stats.mode(speed)

print(f"Mean is {x}")
print(f"Median is {y}")
print(f"Mode is {z}")