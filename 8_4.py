a1=int(input("Enter dimension of matrix A rows followed by columns:"))
a2=int(input())
b1=int(input("Enter dimension of matrix B rows followed by columns:"))
b2=int(input())
assert a2==b1, "Matrix multiplication is not possible for the given dimensions"
A=[[0]*a2 for i in range(a1)]
B=[[0]*b2 for i in range(b1)]
a=[[0]*b2 for i in range(a1)]
print(len(A))

print("Enter elements of matrix A row wise:\n")
for i in range(a1):
    for j in range(a2):
        A[i][j]=int(input())

print("Enter elements of matrix B row wise:\n")
for i in range(b1):
    for j in range(b2):
        B[i][j]=int(input())

for i in range(a1):
   for j in range(b2):
        for k in range(a2):
            a[i][j]+=A[i][k]*B[k][j]

print("The resultant matrix is:\n",a)