def SimpleIntrest(p,r,t):
    print("The principal is ",p)
    print("The time rate of intrest is ",r)
    print("The time period is " ,t)

    si = (p * r * t) / 100

    print("The simple intrest is ",si)

    return si

SimpleIntrest(8,8,6)