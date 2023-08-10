def modify(a):
    a.append(5)
    print("inside",a,id(a))
    
a = [1,2,3,4]
modify(a)
print("Outside ",a,id(a))
