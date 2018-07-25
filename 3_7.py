import random as r

li=[21,26,54]
x=int(input("Enter the number of random numbers to append:"))
for i in range(1,x):
    li.append(r.randint(1,20))
print(li)