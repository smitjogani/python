# Compound intrest 

def CompoundIntrest(principle,rate,time):
    Amount = principle * (pow(1 + rate / 100 , time))
    CI = Amount - principle
    print("Compound Intrest is" , CI)

CompoundIntrest(10000, 10.25, 5)
