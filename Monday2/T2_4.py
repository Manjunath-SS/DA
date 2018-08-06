import numpy as np

twoD=np.random.randint(10, size=(2,4))

print("The array is:\n",twoD)

#a) Print the dimensions of the array
print("The dimension of the array:",twoD.shape)

#b) Update the array by changing the dimension to 3D
threeD=twoD.reshape(2,1,4)
print("\n\n\n Updating 2D into 3D array:\n", threeD)
print("The dimension of the array:",threeD.shape)

#c) Add 5 to every element, subtract 2 from each element, multiply each element by 5
#NOTE: All these operations are not successive, they are performed on "threeD" array whose contents remain unaltered
print("\n\n\n Adding 5 to every element:\n",np.add(threeD,5))
print("\n Subtracting 2 from each element:\n",np.add(threeD,-2))
print("\n Multiplying each element by 5:\n",np.multiply(threeD,5))