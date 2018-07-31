import numpy as np

x=int(input("Enter no of rows:"))
y=int(input("Enter no of columns:"))

ar=[[0]*y for i in range(x)]

for i in range(x):
    for j in range(y):
        ar[i][j]=int(input())


print("Input array is:",ar)

newAr=np.array(ar)
print(type(newAr))
print("Dimensions of the input array:",newAr.shape)

print("After reshaping:",newAr.reshape((y,x)))

print("Slicing operations:")
print(newAr[0:2,0])

print("Converting into 1D array:")
print(newAr.ravel())

print("Minimum:", newAr.min())
print("Maximum:", newAr.max())
print("Sum:", newAr.sum())

print("Adding 10 to array:",np.add(newAr,10))
print("Multiply array with 5:",np.multiply(newAr,5))
print("Dividing array by 2:",np.divide(newAr,2))