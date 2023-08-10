# calculate age using datetime modual

from datetime import *

d1,m1,y1 = [int(i) for i in input("Enter DOB in DD/MM/YYYY formate : ").split('/')]
print(f"Birth Date is {d1}-{m1}-{y1}")

dt = date(y1,m1,d1)

d = date.today()

print(f"Today date is {d}")

print("Age : ", int(d.strftime("%Y")) - int(dt.strfime("%Y")))