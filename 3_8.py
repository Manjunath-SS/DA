import numpy

li = [int(x) for x in input("Enter list separated by spaces:").split()]
li=sorted(li)
p=numpy.poly1d(li)
print("Roots are:",p.r)