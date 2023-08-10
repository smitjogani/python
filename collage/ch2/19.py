# 2-19. Create a program to sort tuple with nested tuples.
tpl = ((8,1,2), (5,4,7), (9,2,10))
print("Unsorted tuple: {}\nSorted tuple (on the 0th element): {}\nSorted tuple (on the 1st element): {}".format(tpl,sorted(tpl), sorted(tpl, key=lambda nst_tpl: nst_tpl[1])))
