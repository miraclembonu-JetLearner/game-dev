matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

print (matrix[1])
print(len(matrix))
print(len(matrix[2]))
print(matrix[2],[2])

A = [[2,4,5],[3,8,12],[2,0,3]]

B = [[1,3,2],[4,1,3],[2,2,2]]

c=[]

for i in range(len(A)):
    row=[]
    for j in range (len(A[0])):
        row.append(A[i][j]+B[i][j])
        c.append(row)
    print(c)


for i in range(len(A)):
    row=[]
    for j in range (len(A[0])):
        row.append(A[i][j]-B[i][j])
        c.append(row)
    print(c)

