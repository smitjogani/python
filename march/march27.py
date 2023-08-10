# Addition of two matrices

x = [[1,2,3],[4,5,6],[7,8,9]]

y = [[1,2,3],[4,5,6],[7,8,9]]

c = [[0,0,0],[0,0,0],[0,0,0]]

# interate through rows
for i in range(len(x)):
    for j in range(len(x[0])):
        c[i][j] = x[i][j] + y[i][j]

for s in c:
    print(s)
