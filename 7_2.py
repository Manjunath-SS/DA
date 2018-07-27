A =[[3, 5, 6],
    [4, 8, 10],
    [2, 1, 8]]
 
I = [[1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]]


print("Matrix A is:\n",A)

a = [[0] * 3 for i in range(3)]

for i in range(len(A)):
    for j in range(len(I)):
        for k in range(len(I)):
            a[i][j]+=A[i][k]*I[k][j]
        
print("\n\nMatrix A.I is:\n",a)

assert a==A,"A!=A.I"
print("\n\nSince assertion is true: Hence proved thatA=A.I") 