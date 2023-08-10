# Python Program to Check the File Size


# using os modual
import os

file_strt = os.stat('./Smit.txt')
print(file_strt.st_size)

# using pathlib modual

from pathlib import Path

file = Path('./Smit.txt')
print(file.stat().st_size)